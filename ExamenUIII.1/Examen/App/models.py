from django.db import models

class Productos(models.Model):
    tipos_choices =  (('Automotriz','Automotriz'), ('Micro tecnologia','Micro tecnologia'))
    estatus_choices = (('Aprobado','Aprobado'),('No aprobado','No aprobado'))
    typeProduc = models.CharField(max_length = 255, choices = tipos_choices)
    estatus = models.CharField(max_length = 255, choices = estatus_choices)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.estatus

class ordenes(models.Model):
    tipos_choices =  (('Automotriz','Automotriz'), ('Micro tecnologia','Micro tecnologia'))
    estatus_choices = (('Abierto','Abierto'),('Cerraro','Cerraro'),('Pendiente','Pendiente'))
    tipo = models.CharField(max_length = 255, choices = tipos_choices)
    solicito =  models.CharField(max_length = 255)
    estatus = models.CharField(max_length = 255, choices = estatus_choices)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.solicito

class Personal(models.Model):
    tipos_choices =  (('Automotriz','Automotriz'), ('Micro tecnologia','Micro tecnologia'))
    name = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    puesto =  models.CharField(max_length = 255)
    linea = models.CharField(max_length = 255, choices = tipos_choices)

    def __str__(self):
        return self.name

class LineaProduccion(models.Model):
    tipos_choices =  (('Automotriz','Automotriz'), ('Micro tecnologia','Micro tecnologia'))
    estado_choices = (('En produccion','En produccion'),('Detenido','Detenido'))
    type = models.CharField(max_length = 255,choices = tipos_choices)
    Producto = models.CharField(max_length = 255)
    jefe = models.ManyToManyField(Personal, related_name='jefe')
    calidad = models.ManyToManyField(Personal, related_name='calidad')
    estado = models.CharField(max_length = 255, choices = estado_choices)
    
    def __str__(self):
        return self.Producto



class Entrega(models.Model):
    entrega = models.ForeignKey(Personal, on_delete = models.CASCADE, related_name='creator')
    recibe = models.ForeignKey(Personal, on_delete = models.CASCADE, related_name='assignee')
    fecha = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.entrega

class Almacen(models.Model):
    tipos_choices =  (('Automotriz','Automotriz'), ('Micro tecnologia','Micro tecnologia'))
    PiezaName = models.CharField(max_length = 255)
    cantidad = models.IntegerField()
    typeProduc = models.CharField(max_length = 255,choices = tipos_choices)
    entregas = models.ForeignKey(Entrega, on_delete= models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.PiezaName




