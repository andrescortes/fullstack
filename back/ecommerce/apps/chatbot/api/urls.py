from django.urls import path

from apps.chatbot.api.views.views import ChatbotAPIView, ChatbotStreamView

urlpatterns = [
    path("normal", ChatbotAPIView.as_view(), name="chatbot_normal"),
    path("stream", ChatbotStreamView.as_view(), name="chatbot_stream"),
]