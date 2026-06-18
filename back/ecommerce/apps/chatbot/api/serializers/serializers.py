from rest_framework import serializers

from apps.chatbot.models import Message, Conversation


class MessageSerializer(serializers.ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta class"""
        model = Message
        fields = ["id", "role", "content", "created_date"]


class ConversationSerializer(serializers.ModelSerializer):
    """Conversation Serializer"""
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        """Meta class"""
        model = Conversation
        fields = ["id", "title", "created_date", "updated_date", "messages"]
