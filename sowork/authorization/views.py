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
        return redirect('user_profile')


# авторизация пользователя
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        return reverse_lazy('user_profile')
