from django.http import HttpResponse
from django.shortcuts import render


def friends(request):
    return render(request, 'friends/friends_list.html')
