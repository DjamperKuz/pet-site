from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Chat, Message
from .forms import MessageForm
import hashlib


def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'messenger/chat_list.html', {'chats': chats})


def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['message_content']
            sender = request.user
            Message.objects.create(chat=chat, sender=sender, content=content)
            return redirect('chat_detail', chat_id=chat_id)
    else:
        form = MessageForm()

    return render(request, 'messenger/chat_detail.html', {'chat': chat, 'messages': messages, 'form': form})


def open_or_create_chat(request, username):
    # найти пользователя с указанным username
    other_user = get_object_or_404(User, username=username)

    # создаём уникальный идентификатор чата на основе участников чата
    participant_ids = sorted([request.user.id, other_user.id])
    unique_id = hashlib.md5(','.join(map(str, participant_ids)).encode()).hexdigest()

    # проверить, существует ли указанный чат
    chat = Chat.objects.filter(participants=request.user).filter(participants=other_user).first()

    # проверяем, есть ли чат с таким идентификатором
    chat, created = Chat.objects.get_or_create(unique_id=unique_id)

    # если чат создан, добавляем участников
    if created:
        chat.participants.add(request.user, other_user)

    # перенаправляем пользователя на страницу чата
    return redirect('chat_detail', chat_id=chat.id)
