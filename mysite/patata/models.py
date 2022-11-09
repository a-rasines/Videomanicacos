from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length= 50)
    def __str__(self) -> str:
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    url_p = models.TextField(default = "")
    def __str__(self) -> str:
        return self.nombre

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_salida = models.IntegerField()
    pegi = models.IntegerField()
    comanya = models.CharField(max_length=50)
    url_v = models.TextField(default = "")

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataforma = models.ManyToManyField(Plataforma)

    def __str__(self) -> str:
        return self.nombre