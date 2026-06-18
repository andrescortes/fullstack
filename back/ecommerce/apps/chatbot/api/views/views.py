import logging

from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chatbot.api.services.llm import call_llm, llama_stream
from apps.chatbot.api.services.web_search import web_search
from apps.chatbot.api.utils.promp_helper import build_messages
from apps.chatbot.models import Conversation, Message
from apps.users.models import User

logger = logging.getLogger('drf_logger')


class ChatbotAPIView(APIView):
    """Chatbot API view"""

    def post(self, request: Request, *args, **kwargs):
        user_question = request.data.get("question")
        conversation_id = request.data.get("conversationId")
        user_id = request.data.get("userId")
        logger.info(f"question: {user_question}, conversation_id: {conversation_id}, user_id: {user_id}")
        if not user_question or not user_id:
            return Response({"error": "Please provide a question"}, status=400)

        user = get_object_or_404(User, id=user_id)

        if conversation_id:
            try:
                conversation = Conversation.objects.get(id=conversation_id, user=user)
            except Conversation.DoesNotExist:
                return Response({"error": "Conversation does not exist"}, status=400)
        else:
            conversation = Conversation.objects.create(user=user, title=user_question)

        history_qs = conversation.messages.all().order_by("-created_date")[:10]
        history_qs = list(reversed(history_qs))

        logger.info(f"message histories: {history_qs}")

        search_context = web_search(user_question, max_results=3)
        logger.info(f"Context from web_search: {search_context}")
        llm_messages = build_messages(user_question, search_context, history_qs)
        Message.objects.create(
            conversation=conversation,
            role="user",
            content=user_question,
        )

        assistant_answer = call_llm(llm_messages)

        Message.objects.create(
            conversation=conversation,
            role="assistant",
            content=assistant_answer,
        )
        conversation.summary = assistant_answer
        conversation.save(update_fields=["summary"])
        return Response({
            "conversationId": conversation.id,
            "user": user.username,
            "answer": assistant_answer,
        }, status=status.HTTP_200_OK)


class ChatbotStreamView(APIView):
    """Chatbot API view Streaming"""

    def post(self, request: Request, *args, **kwargs):
        """Method post"""

        user_question = request.data.get("question")
        conversation_id = request.data.get("conversationId")
        user_id = request.data.get("userId")

        if not user_question or not user_id:
            return StreamingHttpResponse(
                iter([b"data: error: missing question or userId\n\n"]),
                content_type="text/event-stream",
            )

        user = get_object_or_404(User, id=user_id)
        # Get or create conversation
        if conversation_id:
            conversation = Conversation.objects.filter(id=conversation_id, user=user).first()
            if conversation is None:
                return StreamingHttpResponse(
                    iter([b"data: error: conversation not found\n\n"]),
                    content_type="text/event-stream",
                )
        else:
            conversation = Conversation.objects.create(user=user, title="New conversation")

        conversation.summary = user_question
        conversation.save(update_fields=["summary"])
        # History
        history_qs = conversation.messages.all().order_by("-created_date")[:10]
        history_qs = list(reversed(history_qs))

        # Save user message (DB)
        Message.objects.create(
            conversation=conversation,
            role="user",
            content=user_question,
        )

        # Web search
        search_context = web_search(user_question, max_results=5)

        # Build messages for LLM
        llm_messages = build_messages(user_question, search_context, history_qs)

        # Generator that forwards llama-server SSE as our SSE
        def event_stream():
            """
            Event stream
            """
            try:
                # forward stream from llama-server
                for line in llama_stream(llm_messages):
                    # Example: "data: {json}\n"
                    if line.startswith("data: "):
                        yield f"{line}\n\n"
                    else:
                        # ensure it's valid SSE
                        yield f"data: {line}\n\n"

                # end-of-stream marker (optional)
                yield "data: [DONE]\n\n"
            except Exception as e:
                yield f"data: error: {str(e)}\n\n"

        response = StreamingHttpResponse(
            streaming_content=event_stream(),
            content_type="text/event-stream",
        )
        # Recommended SSE headers
        response["Cache-Control"] = "no-cache"
        response["X-Accel-Buffering"] = "no"  # disable buffering in some proxies
        return response
