from django.http import HttpResponse
from django.shortcuts import render


def lenta(request):
    return HttpResponse('Лента')
# Create your views here.
