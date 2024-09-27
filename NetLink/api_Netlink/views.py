from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from api_Netlink.models import laboralInformation
from .serializer import laboralInformationSerializer

class laboralInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        laboralList = laboralInformation.objects.all()
        laboralSerializer = laboralInformationSerializer(laboralList, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data ={
            'latestPosition':request.data.get('latestPosition'),
            'abilities':request.data.get('skills'),
            'previousExperiences':request.data.get('previousExperiences'),
            'isLooking':request.data.get('lookingForEmployement'),
            'desiredPosition':request.data.get('desiredPosition'),
            'desiredCountry':request.data.get('desiredCountry'),
            'telecommuting':request.data.get('telecommuting')
        }
        serializer = laboralInformationSerializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)