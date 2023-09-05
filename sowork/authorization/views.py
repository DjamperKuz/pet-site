from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return HttpResponse('Страница регистрации')


def login(request):
    return HttpResponse('Страница авторизации')
# Create your views here.
