import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from api_Netlink.models import publicacion
from .serializer import publicacion_serializer
from django.shortcuts import render

# Create your views here.
#Clase publicacion view
class PublicacionView(APIView):
    def get(self, request, *args, **kwargs):
            lista_publicaciones=publicacion.objects.all()
            serializer_publicaciones=publicacion_serializer(lista_publicaciones, many=True)
            return Response(serializer_publicaciones.data,status=status.HTTP_200_OK)
    def post(self, resquest, *args, **kwargs):
            data={
                'titulo':resquest.data.get('titulo'),
                'descripcion':resquest.data.get('descripcion'),
                'multimedia':resquest.data.get('multimedia'),
            }
            serializador=publicacion_serializer(data=data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    ##seguir con metodo put