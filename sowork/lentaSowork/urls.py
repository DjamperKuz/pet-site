from django.urls import path
from . import views


urlpatterns = [
    path('', views.lenta, name='main_page'),
]
