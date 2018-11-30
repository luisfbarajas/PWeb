from django.db import models


# class Administradores(models.Model):
#     nombres = models.CharField(max_length=255)
#     ApellidoMat = models.CharField(max_length=255)
#     ApellidoPat = models.CharField(max_length=255)
#     email = models.CharField(max_length = 255)
#     password = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.nombres


# class Usuarios(models.Model):
#     nombres = models.CharField(max_length=255)
#     ApellidoMat = models.CharField(max_length=255)
#     ApellidoPat = models.CharField(max_length=255)
#     email = models.CharField(max_length = 255)
#     password = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.nombres


class UsuariosClientes(models.Model):
    nombres = models.CharField(max_length=255)
    ApellidoMat = models.CharField(max_length=255)
    ApellidoPat = models.CharField(max_length=255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombres



class RegistroProyecto(models.Model):
    NombreProyecto = models.CharField(max_length = 255)
    NombreEmpresa = models.CharField(max_length = 255)
    representante = models.CharField(max_length = 255)
    departamento = models.CharField(max_length = 255)
    FechaRegistro = models.DateField(auto_now_add=True)
    inicia = models.DateField()
    finaliza = models.DateField()
    descripcion = models.CharField(max_length = 255)
    ObjGeneral = models.CharField(max_length = 255)
    vision = models.CharField(max_length = 255)
    # administrador = models.ForeignKey(Administradores, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.NombreProyecto