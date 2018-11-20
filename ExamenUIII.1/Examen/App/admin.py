from django.contrib import admin
from .models import Personal, Productos,LineaProduccion, Entrega, Almacen,ordenes

# Register your models here.
admin.site.register(Personal)
admin.site.register(Productos)
admin.site.register(LineaProduccion)
admin.site.register(Entrega)
admin.site.register(Almacen)
admin.site.register(ordenes)
