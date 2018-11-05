from django.db import models


class empleados(models.Model):
    name = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    carrera = models.CharField(max_length = 255)
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class actividades(models.Model):
    name = models.CharField(max_length=255)
    duracion = models.IntegerField()
    empleado = models.ForeignKey(empleados, on_delete = models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class RegistroProyecto(models.Model):
    name = models.CharField(max_length = 255)
    lider = models.CharField(max_length = 255)
    inicia = models.DateField()
    duracion = models.IntegerField()
    reuniones = models.CharField(max_length = 255)
    trabaja = models.ForeignKey(empleados, on_delete = models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


