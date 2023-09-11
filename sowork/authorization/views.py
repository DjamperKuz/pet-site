from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *


# регистрация пользователя
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authorization/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        # Собираем URL для профиля пользователя
        profile_url = reverse_lazy('user_profile', kwargs={'username': user.username})

        # Перенаправляем пользователя на его профиль
        return redirect(profile_url)


# авторизация пользователя
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        # Получаем username авторизованного пользователя
        username = self.request.user.username
        # Собираем URL для профиля пользователя
        profile_url = reverse_lazy('user_profile', kwargs={'username': username})
        return profile_url
