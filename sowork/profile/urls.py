from django.urls import path
from . import views


urlpatterns = [
    path('profile/<slug:username>/', views.profile, name='user_profile'),
    path('logout/', views.logout_user, name='logout'),
    path('profile-update/', views.profile_update, name='profile_update')
]
