from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_materno=models.CharField(max_length=30)
    apellido_paterno=models.CharField(max_length=30)
    edad=models.IntegerField()
    email=models.CharField(max_length=30)
    telefono=models.CharField(max_length=10)
