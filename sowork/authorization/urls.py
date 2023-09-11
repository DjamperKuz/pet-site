from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]
