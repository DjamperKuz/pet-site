from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


def profile(request, username):
    post = get_object_or_404(User, username=username)

    return render(request, 'profile/user_profile.html', context={'username': post})

