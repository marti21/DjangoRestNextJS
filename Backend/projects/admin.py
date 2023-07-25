from django.contrib import admin
from .models import Pelicula, SolicitudAmistad, Usuario

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(SolicitudAmistad)
admin.site.register(Usuario)