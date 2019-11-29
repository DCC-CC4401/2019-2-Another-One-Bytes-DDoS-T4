from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(unique=False,max_length=200)
    apellido = models.CharField(unique=False, max_length=200)
    hash = models.CharField(unique=True,max_length=200)
    correo = models.EmailField(max_length=50, null=False, blank=False)

