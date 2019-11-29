from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import Usuario

class Admin(UserAdmin):
    model = Usuario
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(Usuario, Admin)