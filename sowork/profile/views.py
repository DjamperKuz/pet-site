from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


@login_required(login_url='/')
def profile(request, username):
    post = get_object_or_404(User, username=username)

    return render(request, 'profile/user_profile.html', context={'username': post})


def logout_user(request):
    logout(request)

    return redirect('login')

