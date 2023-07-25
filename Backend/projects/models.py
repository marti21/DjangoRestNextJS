from django.db import models
from enum import Enum
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, date


class Genero(Enum):
    ACCION = 'Accion'
    AVENTURA = 'Aventura'

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(default="", null=True, blank=True)
    genero = models.CharField(max_length=20, choices=[(genero.value, genero.name) for genero in Genero])
    director = models.CharField(max_length=200, default="", null=True)
    año_estreno = models.DateField(default=timezone.now, null=True, blank=True)
    duracion =  models.DurationField(null=True)
    puntuacion = models.IntegerField(default=0)

class Usuario(User):
    imagen_perfil = models.ImageField(upload_to='userImages', null=True, blank=True)
    my_date_field = models.DateField(default=date.today())

class SolicitudAmistad(models.Model):
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='destinatario')
    recipiente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recipiente')
