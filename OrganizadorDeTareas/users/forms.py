# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import Usuario

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('correo', 'nombre','apellido')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('correo', 'password')



