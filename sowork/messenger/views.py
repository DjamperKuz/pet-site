from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message
from .forms import MessageForm


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
