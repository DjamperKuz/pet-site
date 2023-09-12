from django.db import models
from django.contrib.auth.models import User
import uuid


class ChatManager(models.Manager):
    def user_chats(self, user):
        return self.filter(participants=user)


class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats', limit_choices_to= \
        {'chats__participants__count': 2})

    # поле для хранения уникального идентификатора чата
    unique_id = models.UUIDField(default=None, null=True, unique=True)

    objects = ChatManager


class MessageManager(models.Manager):
    def chat_messages(self, chat):
        return self.filter(chat=chat)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = MessageManager
