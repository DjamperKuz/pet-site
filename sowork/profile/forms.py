from .models import Profile
from django import forms


class ProfileUpdateAvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
