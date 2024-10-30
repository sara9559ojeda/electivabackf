from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from Cuentas.models import laboralInformation
from django.db import models
from Cuentas.models import Experience, AcademicInformation, Usuario
from Cuentas.serializer import laboralInformationSerializer, academicInformationSerializer, usuario_serializer

class laboralInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        laboralList = laboralInformation.objects.all()
        laboralSerializer = laboralInformationSerializer(laboralList, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def getLaboralInfo(self, request, id, *args, **kwargs):
        miLaboralInfo = laboralInformation.objects.filter(id = id).first()
        laboralSerializer = laboralInformationSerializer(miLaboralInfo, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        new_experience = Experience.objects.create(
            company=request.data.get('company'),
            position=request.data.get('position'),
            description=request.data.get('description')
        )
        
        data = {
            'latestPosition':request.data.get('latestPosition'),
            'abilities': request.data.get('abilities'),
            'lookingForEmployement': request.data.get('lookingForEmployement'),
            'desiredPosition': request.data.get('desiredPosition'),
            'desiredCountry': request.data.get('desiredCountry'),
            'telecommuting': request.data.get('telecommuting')
        }
        
        serializer = laboralInformationSerializer(data=data)
        
        if serializer.is_valid():
            laboral_info = serializer.save()
            laboral_info.previousExperiences.add(new_experience)
            laboral_info.save()
            
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
    
    def putAbility(self, request, pkid):
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
    
    def delete(self, request, pkid):
        try:
            laboral_info = laboralInformation.objects.get(id=pkid)
            
            laboral_info.delete()
            
            return Response({"message": "Información laboral eliminada exitosamente."}, status=status.HTTP_200_OK)
        
        except laboralInformation.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)

class academicInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        academicList = AcademicInformation.objects.all()
        academicSerializer = academicInformationSerializer(academicList, many=True)
        return Response(academicSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'educativeInstitution': request.data.get('educativeInstitution'),
            'title': request.data.get('title'),
            'academicDiscipline': request.data.get('academicDiscipline'),
            'startDate': request.data.get('startDate'),
            'endDate': request.data.get('endDate'),
            'aditionalActivities': request.data.get('aditionalActivities'),
            'description': request.data.get('description'),
            'abilities': request.data.get('abilities')
        }
        
        serializer = academicInformationSerializer(data=data)
        
        if serializer.is_valid():
            academic_info = serializer.save()
            
            academic_info.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid):
        try:
            academic_info = AcademicInformation.objects.get(id=pkid)
        except AcademicInformation.DoesNotExist:
            return Response({"error": "Información académica no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        new_activity = request.data.get('aditionalActivities')
        if not new_activity:
            return Response({"error": "Datos de experiencia previos no proporcionados."}, status=status.HTTP_400_BAD_REQUEST)
        
        academic_info.aditionalActivities.append(new_activity)
        
        academic_info.save()

        serializer = academicInformationSerializer(academic_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def putAbility(self, request, pkid):
        try:
            academic_info = AcademicInformation.objects.get(id=pkid)
        except AcademicInformation.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        new_ability= request.data.get('abilities')
        if not new_ability:
            return Response({"error": "Habilidad no proporcionada."}, status=status.HTTP_400_BAD_REQUEST)
        
        academic_info.abilities.append(new_ability)
        
        academic_info.save()

        serializer = academicInformationSerializer(academic_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pkid):
        try:
            academic_info = AcademicInformation.objects.get(id=pkid)
            
            academic_info.delete()
            
            return Response({"message": "Información académica eliminada exitosamente."}, status=status.HTTP_200_OK)
        
        except AcademicInformation.DoesNotExist:
            return Response({"error": "Información académica no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        

class UsuariosView(APIView):
    def get(self, request, *args, **kwargs):
            lista_usuarios=Usuario.objects.all()
            serializer_usuarios=usuario_serializer(lista_usuarios, many=True)
            return Response(serializer_usuarios.data,status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'contraseña': request.data.get('contraseña'),
            'fechaNacimiento': request.data.get('fechaNacimiento'),
            'email': request.data.get('email'),
            'paisOrigen': request.data.get('paisOrigen')       
        }

        serializador = usuario_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(
                {"message": "Usuario creado correctamente", "data": serializador.data},
                status=status.HTTP_201_CREATED
            )
    
        return Response(
            {"message": "El usuario no se pudo crear", "errors": serializador.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pkid):
    # Intenta actualizar el usuario y guarda la cantidad de registros afectados
        registros_actualizados = Usuario.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            contraseña=request.data.get('contraseña'),
            fechaNacimiento=request.data.get('fechaNacimiento'),
            email=request.data.get('email'),
            paisOrigen=request.data.get('paisOrigen')
        )

    # Si se actualizó al menos un registro, devuelve un mensaje de éxito
        if registros_actualizados > 0:
            return Response(
                {"message": "Usuario actualizado correctamente"},
                status=status.HTTP_200_OK
        )
        else:
            return Response(
                {"message": "El usuario no se pudo actualizar"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pkid, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(id=pkid)
            usuario.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
          
class UsuarioQueryApiView(APIView):
    def get(self, request, pkid, *args, **kargs):
        miUsuario=Usuario.objects.filter(id=pkid).first()
        serializer_usuario = usuario_serializer(miUsuario)
        return Response(serializer_usuario.data, status=status.HTTP_200_OK)

