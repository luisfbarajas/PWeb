from django.contrib import admin
from . import models as models_db
# Register your models here.

admin.site.register(models_db.Proyecto)
admin.site.register(models_db.RegistroProyecto)
admin.site.register(models_db.Actividades)
