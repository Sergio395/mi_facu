from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo=models.CharField(max_length=3, primary_key=True) 
    nombre=models.CharField(max_length=50) # tipos de datos que la tabla admitirá
    duracion=models.models.PositiveSmallIntegerField(default=5)
    