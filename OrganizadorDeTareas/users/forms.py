# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import Usuario

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('correo', 'nombre','apellido','foto')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('correo', 'password')

class changeImage(forms.Form):
    foto = forms.ImageField(allow_empty_file=True)




