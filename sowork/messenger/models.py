from django.db import models
from django.contrib.auth.models import User


class ChatManager(models.Manager):
    def user_chats(self, user):
        return self.filter(participants=user)


class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')
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
