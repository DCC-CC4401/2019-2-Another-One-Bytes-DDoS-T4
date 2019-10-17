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
    cat_id = models.ForeignKey(Categoria, models.CASCADE)
    act_id = models.ForeignKey(Actividad, models.CASCADE)


    def __str__(self):
        return self.cla_nombre

class Usuario(models.Model):
    ADMINISTRADOR = "A"
    NATURAL = "N"

    tipo_choice = (
        (ADMINISTRADOR, "administrador"),
        (NATURAL, "natural")
    )

    id = models.IntegerField(primary_key=True)
    hash=models.CharField(max_length=30, unique=True)
    correo = models.EmailField(max_length=50, null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=tipo_choice, default=NATURAL)


class UsuarioNatural(models.Model):
    user_id = models.ForeignKey(Usuario, models.CASCADE)
    user_nombre = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to='fotos')
    fecha_nacimiento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.user_nombre

class Registro(models.Model):
    REALIZANDO = "R"
    FINALIZADO = "F"

    estado_choices = (
        (REALIZANDO, "realizando"),
        (FINALIZADO, "finalizado")
    )

    act_id = models.ForeignKey(Actividad, models.CASCADE)
    user_id = models.ForeignKey(UsuarioNatural, models.CASCADE)
    estado = models.CharField(max_length=1, choices=estado_choices, default=REALIZANDO)

    def __str__(self):
        return self.estado #esta puede cambiar

class Solicitud(models.Model):
    emisor_id = models.ForeignKey(UsuarioNatural, models.CASCADE, related_name="emisor")
    receptor_id = models.ForeignKey(UsuarioNatural, models.CASCADE, related_name="receptor")

class Amistad(models.Model):
    user_id = models.ForeignKey(UsuarioNatural, models.CASCADE, related_name="user")
    amigo_id = models.ForeignKey(UsuarioNatural, models.CASCADE, related_name="amigo")
