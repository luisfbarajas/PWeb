from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('almacen',views.almacen,name = 'almacen'),
    path('lineasProduccion',views.lineasProduccion, name = 'lineasProduccion'),
    path('solicitarMaterial',views.solicitarMaterial, name = 'solicitarMaterial'),
    path('PersonalArea',views.personalArea, name = 'PersonalArea'),
    path('Entregas',views.entregas, name = 'Entregas'),
    path('producto', views.revisados, name = 'producto'),
    path('ordenes',views.orden, name='ordenes'),
    path('productoorden',views.productoorden,name='productoorden'),
]