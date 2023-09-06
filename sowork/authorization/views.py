from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, 'authorization/register.html')


def login(request):
    return render(request, 'authorization/login.html')
# Create your views here.
