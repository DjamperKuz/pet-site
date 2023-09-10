from django.urls import path
from . import views

urlpatterns = [
    path('messenger', views.messenger_home, name='messenger_home'),
    path('messenger_api', views.messenger_api),
]
