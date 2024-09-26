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