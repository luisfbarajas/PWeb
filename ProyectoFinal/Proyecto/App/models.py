from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class empleados(models.Model):
    name = models.CharField(max_length = 255)
    puesto = models.CharField( max_length = 255)
    carrera = models.CharField( max_length = 255)
    antiguedad = models.CharField( max_length = 255)

    def __str__(self):
        return self.name

class RegistroProyecto(models.Model):
    NombreProyecto = models.CharField(max_length = 255)
    Cliente = models.CharField(max_length = 255)
    representante = models.CharField(max_length = 255)
    departamento = models.CharField(max_length = 255 )
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    inicia = models.DateField()
    finaliza = models.DateField()
    descripcion = models.CharField(max_length = 255,null=True, blank=True)
    ObjGeneral = models.CharField(max_length = 255,null=True, blank=True)
    userRegistro = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    status = models.BooleanField(default= True,  null=True, blank=True)
    def __str__(self):
        return self.NombreProyecto

class Actividades(models.Model):
    encargado = models.ForeignKey(empleados, on_delete = models.CASCADE, default = '1')
    actividadName = models.CharField(max_length = 255)
    actividad_tipo =  (('Individual','Individual'), ('Multiple','Multiple'))
    estado_tipo = (('Pendiente','Pendiente'),('Asignada','Asignada'),('Cancelada','Cancelada'))
    type = models.CharField(max_length = 255,choices = actividad_tipo)
    estado = models.CharField(max_length = 255, choices = estado_tipo)
    inicia = models.DateField(null=True, blank=True)
    finaliza = models.DateField(null=True, blank=True)
    proyecto = models.ForeignKey(RegistroProyecto,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.actividadName
