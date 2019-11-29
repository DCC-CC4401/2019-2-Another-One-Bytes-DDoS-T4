from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import Usuario

class Admin(UserAdmin):
    model = Usuario
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


    list_display = ('nombre','apellido','correo','is_staff')  # Contain only fields in your `custom-user-model`
    list_filter = ('nombre','apellido','correo','is_staff')  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ('nombre','apellido','correo','is_staff')  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ('nombre','apellido','correo','is_staff')  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = ()  # Leave it empty. You have neither `groups` or `user_permissions`
    fieldsets = (

    )

admin.site.register(Usuario, Admin)