from django.http import HttpResponse
from django.shortcuts import render


def profile(request):
    return render(request, 'profile/main_page.html')
# Create your views here.
