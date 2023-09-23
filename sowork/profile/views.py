from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ProfileUpdateAvatarForm


@login_required(login_url='/')
def profile(request, username):
    post = get_object_or_404(User, username=username)
    current_user = request.user

    return render(request, 'profile/user_profile.html', context={'username': post, 'current_user': current_user})


def logout_user(request):
    logout(request)

    return redirect('login')


@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateAvatarForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile_update')

    else:
        p_form = ProfileUpdateAvatarForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'profile/update_profile.html', context)
