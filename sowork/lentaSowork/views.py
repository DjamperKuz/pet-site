from django.http import HttpResponse
from django.shortcuts import render


def lenta(request):
    return render(request, 'lentaSowork/main_page.html')
# Create your views here.
