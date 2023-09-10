from django.shortcuts import render
from django.http import JsonResponse


def messenger_home(request):
    return render(request, "index.html")


def messenger_api(request):
    pass
