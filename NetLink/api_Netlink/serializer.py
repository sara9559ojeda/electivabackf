from api_Netlink.models import publicacion
from rest_framework import serializers

#Serializer publicacion para feed de publicaciones
class publicacion_serializer(serializers.ModelSerializer):
    class Meta:
        model=publicacion
        fields=[
            'titulo',
            'descripcion',
            'multimedia',
            'fecha'
        ]