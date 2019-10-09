from django.db import models

class Actividad(models.Model):
    act_id = models.IntegerField(primary_key=True, null=False, blank=False)
    nombre_act = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.TextField(null=False)
    fecha = models.DateField(auto_now=True, null=False, blank=False)
    hora_inicio = models.DateTimeField(auto_now=True, null=False, blank=False) #tal vez deba ser corregido
    duracion = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.nombre_act

class Categoria(models.Model):
    cat_id = models.IntegerField(primary_key=True, null=False, blank=False)
    nombre_cat = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nombre_cat

class Clasificacion(models.Model):
    cat_id = models.OneToOneField(Categoria)
    act_id = models.OneToOneField(Actividad)
    cla_nombre = models.CharField(primary_key=True, null=False, blank=False)

    def __str__(self):
        return self.cla_nombre

class Usuario(models.Model):
    ADMINISTRADOR = "A"
    NATURAL = "N"

    tipo_choice = (
        (ADMINISTRADOR, "administrador")
        (NATURAL, "natural")
    )

    id = models.IntegerField(primary_key=True)
    #falta hacer el hashign de la contraseña
    correo = models.EmailField(max_length=75, null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=tipo_choice, default=NATURAL)


class UsuarioNatural(models.Model):
    user_id = models.OneToOneField(Usuario)
    user_nombre = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to='/fotos')
    fecha_nacimiento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.user_nombre

class Registro(models.Model):
    REALIZANDO = "R"
    FINALIZADO = "F"

    estado_choices = (
        (REALIZANDO, "realizando")
        (FINALIZADO, "finalizado")
    )

    act_id = models.OneToOneField(Actividad)
    user_id = models.OneToOneField(UsuarioNatural)
    estado = models.CharField(max_length=1, choices=estado_choices, default=REALIZANDO)

    def __str__(self):
        return self.estado #esta puede cambiar

class Solicitud(models.Model):
    emisor = models.OneToOneField(UsuarioNatural)
    receptor = models.OneToOneField(UsuarioNatural)

class Amistad(models.Model):
    user_id = models.OneToOneField(UsuarioNatural)
    amigo_id = models.OneToOneField(UsuarioNatural)

