from django.shortcuts import render, get_object_or_404
from .models import Chat, Message


def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'messenger/chat_list.html', {'chats': chats})


def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat)
    return render(request, 'messenger/chat_detail.html', {'chat': chat, 'messages': messages})
