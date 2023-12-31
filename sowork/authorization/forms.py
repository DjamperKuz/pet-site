from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# регистрация пользователя
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form_input',
                                                                       'placeholder': 'Логин'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form_input',
                                                                     'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form_input',
                                                                            'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form_input',
                                                                            'placeholder': 'Подтвердите пароль'}))

    # проверка email на уникальность
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Пользователь с таким email уже зарегистрирован')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# авторизация пользователя
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form_input',
                                                                       'placeholder': 'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form_input',
                                                                           'placeholder': 'Пароль'}))
