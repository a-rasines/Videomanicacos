from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length= 50)

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_salida = models.DateField()
    pegi = models.IntegerField()
    comanya = models.CharField(max_length=50)

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataforma = models.ManyToManyField(Plataforma)