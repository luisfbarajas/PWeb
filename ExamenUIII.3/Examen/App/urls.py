from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('empleados',views.empleadoss,name = 'empleados'),
    path('Reuniones',views.reunion, name='Reuniones'),
    path('empeladoProyecto', views.empleadoProyecto, name='empeladoProyecto'),
    path('actividadEmpleado', views.actividadEmpleado, name ='actividadEmpleado')
]