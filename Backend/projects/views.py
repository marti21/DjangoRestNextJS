from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.shortcuts import get_object_or_404
from .models import Pelicula, Genero, SolicitudAmistad, Usuario
from .serializers import PeliculasSerializer, SolicitudesAmistadSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


##http://127.0.0.1:8000/api/movies/by_genre/?format=api&genre=Accion&page=1&page_size=1

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_all_films(request):
    try: 
        peliculas = Pelicula.objects.all()
        print(Genero.AVENTURA)

    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        paginator = PageNumberPagination()
        page_size = request.GET.get('page_size')  # Obtener el tamaño de página de la URL
        paginator.page_size = int(page_size) if page_size else paginator.page_size  # Si no se proporciona, usa el tamaño de página predeterminado
        paginated_peliculas = paginator.paginate_queryset(peliculas, request)

        serializefilms = PeliculasSerializer(paginated_peliculas,many=True, context={'request':request})
        return Response(data=serializefilms.data, status=status.HTTP_200_OK)
        

@api_view(['GET'])
def get_genero_films(request):
    try:
        peliculas = Pelicula.objects.filter(genero=request.GET.get('genre'))
    
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        paginator = PageNumberPagination()
        page_size = request.GET.get('page_size')  # Obtener el tamaño de página de la URL
        paginator.page_size = int(page_size) if page_size else paginator.page_size  # Si no se proporciona, usa el tamaño de página predeterminado
        paginated_peliculas = paginator.paginate_queryset(peliculas, request)

        serilizedFilms = PeliculasSerializer(paginated_peliculas,many=True,context={'request':request})
        return Response(data=serilizedFilms.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_friend_requests(request):
    try:
        solicitudes = SolicitudAmistad.objects.all()
    except SolicitudAmistad.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serilizedSolicitudesAmistad = SolicitudesAmistadSerializer(solicitudes,many=True,context={'request':request})
        return Response(data=serilizedSolicitudesAmistad.data, status=status.HTTP_200_OK)

class Protegida(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"content": "Esta vista está protegida MAAAA"})

@api_view(['GET'])
def obtener_usuarios(request):
    try:
        usuarios = Usuario.objects.all()
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serilizedUsuarios = UserSerializer(usuarios,many=True,context={'request':request})
        return Response(data=serilizedUsuarios.data, status=status.HTTP_200_OK)