from rest_framework import serializers
from .models import Pelicula, SolicitudAmistad, Usuario

class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['pk','titulo','descripcion','genero','director','año_estreno','duracion','puntuacion']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email','imagen_perfil','first_name','last_name','date_joined')

class SolicitudesAmistadSerializer(serializers.ModelSerializer):
    destinatario = UserSerializer()
    recipiente = UserSerializer()
    
    class Meta:
        model = SolicitudAmistad
        fields = ['pk','destinatario','recipiente']