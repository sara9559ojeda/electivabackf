from django.db import models
from datetime import datetime

# Create your models here.
#Clase publicacion para feed de publicaciones
class publicacion(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    multimedia=models.CharField(max_length=200)
    fecha=models.DateTimeField()
    