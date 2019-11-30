from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin

from django.contrib.auth.base_user import BaseUserManager
from django.db import models



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, correo, nombre,apellido,password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not correo:
            raise ValueError('The given email must be set')
        email = self.normalize_email(correo)
        user = self.model(correo=email,nombre=nombre,apellido=apellido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, correo, nombre,apellido,password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(correo,nombre,apellido, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):


    nombre=models.CharField(unique=False,max_length=200)
    apellido = models.CharField(unique=False, max_length=200)
    correo = models.EmailField(unique=True,max_length=50, null=False, blank=False,verbose_name=u"Correo Electrónico")
    foto = models.ImageField(upload_to='images/',verbose_name=u"Foto de perfil")
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('is_staff'), default=False)

    objects = UserManager()

    #EMAIL_FIELD = 'correo'
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','apellido']

    class Meta:
        verbose_name = ('usuario')
        verbose_name_plural = ('usuarios')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.nombre, self.apellido)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.nombre
    def set_foto(self,foto):
        self.foto=foto
