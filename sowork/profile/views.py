from django.http import HttpResponse
from django.shortcuts import render


def profile(request):
    username = request.user.username

    return render(request, 'profile/user_profile.html', context={'username': username})
# Create your views here.
