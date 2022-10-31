from django.db import models

# Create your models here.

class Registrar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    celular = models.CharField(max_length=30)

class turno(models.Model):
    usuario=models.IntegerField()
    