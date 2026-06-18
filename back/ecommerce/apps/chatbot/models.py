from django.conf import settings
from django.db import models

from apps.base.models import BaseModel

# Create your models here.

User = settings.AUTH_USER_MODEL


class Conversation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    title = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)

    class Meta:
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"

    def __str__(self):
        return self.title or f"Conversation: {self.id} with user: {self.user}"


class Message(BaseModel):
    ROLE_CHOICES = (
        ("user", "User"),
        ("assistant", "Assistant"),
        ("system", "system"),
    )
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.role}]: {self.content[:50]}"
