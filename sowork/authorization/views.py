from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, 'authorization/register')


def login(request):
    return render(request, 'authorization/login')
# Create your views here.
