from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

class Juego(models.Model):
    nombre_juego = models.CharField(max_length=50)
    precio = models.IntegerField()
    sinopsis = models.CharField(max_length = 100)

class Consola(models.Model):
    nombre_consola = models.CharField(max_length = 50)
    precio = models.IntegerField()
