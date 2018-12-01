from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RegistroProyecto(models.Model):
    NombreProyecto = models.CharField(max_length = 255)
    NombreEmpresa = models.CharField(max_length = 255)
    representante = models.CharField(max_length = 255)
    departamento = models.CharField(max_length = 255 )
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    inicia = models.DateField()
    finaliza = models.DateField()
    descripcion = models.CharField(max_length = 255,null=True, blank=True)
    ObjGeneral = models.CharField(max_length = 255,null=True, blank=True)
    vision = models.CharField(max_length = 255)
    proRegistro = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    status = models.BooleanField(default= True,  null=True, blank=True)
    def __str__(self):
        return self.NombreProyecto


class Proyecto(models.Model):
    NombreProyecto = models.CharField(max_length = 255)
    representante = models.CharField(max_length = 255)
    empresa =  models.CharField(max_length = 255)
    
    def __str__(self):
        return self.NombreProyecto

class Actividades(models.Model):
    actividad_tipo =  (('Individual','Individual'), ('Multiple','Multiple'))
    estado_tipo = (('Pendiente','Pendiente'),('Asignada','Asignada'),('Cancelada','Cancelada'))
    type = models.CharField(max_length = 255,choices = actividad_tipo)
    representante = models.ManyToManyField(Proyecto, related_name='representant')
    estado = models.CharField(max_length = 255, choices = estado_tipo)
    
    def __str__(self):
        return self.estado

