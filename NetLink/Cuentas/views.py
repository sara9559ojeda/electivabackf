from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from Cuentas.models import laboralInformation
from django.db import models
from Cuentas.models import Experience
from Cuentas.serializer import laboralInformationSerializer

class laboralInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        laboralList = laboralInformation.objects.all()
        laboralSerializer = laboralInformationSerializer(laboralList, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        # Crear la nueva experiencia como latestPosition
        new_experience = Experience.objects.create(
            company=request.data.get('company'),
            position=request.data.get('position'),
            description=request.data.get('description')
        )
        
        # Preparar los datos para crear laboralInformation
        data = {
            'latestPosition': {  # Aquí enviamos un diccionario con los detalles de la nueva experiencia
                'company': new_experience.company,
                'position': new_experience.position,
                'description': new_experience.description
            },
            'abilities': request.data.get('abilities'),
            'lookingForEmployement': request.data.get('lookingForEmployement'),
            'desiredPosition': request.data.get('desiredPosition'),
            'desiredCountry': request.data.get('desiredCountry'),
            'telecommuting': request.data.get('telecommuting')
        }
        
        # Crear la nueva instancia de laboralInformation
        serializer = laboralInformationSerializer(data=data)
        
        if serializer.is_valid():
            laboral_info = serializer.save()  # Guardar la nueva información laboral
            
            # Agregar la nueva experiencia al conjunto de experiencias previas
            laboral_info.previousExperiences.add(new_experience)
            laboral_info.save()  # Guardar los cambios
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid):
        try:
            laboral_info = laboralInformation.objects.get(id=pkid)
        except laboralInformation.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        new_experience_data = request.data.get('previousExperiences')
        if not new_experience_data:
            return Response({"error": "Datos de experiencia previos no proporcionados."}, status=status.HTTP_400_BAD_REQUEST)
        
        new_experience = Experience.objects.create(
            company=new_experience_data.get('company'),
            position=new_experience_data.get('position'),
            description=new_experience_data.get('description')
        )
        
        laboral_info.previousExperiences.add(new_experience)
        
        laboral_info.save()

        serializer = laboralInformationSerializer(laboral_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pkid):
        try:
            laboral_info = laboralInformation.objects.get(id=pkid)
        except laboralInformation.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        new_ability= request.data.get('abilities')
        if not new_ability:
            return Response({"error": "Datos de experiencia previos no proporcionados."}, status=status.HTTP_400_BAD_REQUEST)
        
        laboral_info.abilities.append(new_ability)
        
        laboral_info.save()

        serializer = laboralInformationSerializer(laboral_info)
        return Response(serializer.data, status=status.HTTP_200_OK)