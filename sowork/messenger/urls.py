from django.urls import path
from . import views

urlpatterns = [
    path('chats', views.chat_list, name='chat_list'),
    path('chats/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('chats/<str:username>/', views.open_or_create_chat, name='open_or_create_chat'),
]
