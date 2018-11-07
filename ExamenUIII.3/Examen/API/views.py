from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, generics, permissions
from App.models import empleados, actividades,RegistroProyecto
from .Serializers import empleadosSerializer, RegistroProyectoSerializer, actividadesSerializer


class empleadosView(viewsets.ModelViewSet):
    queryset = empleados.objects.all()
    serializer_class = empleadosSerializer


class actividadesView(viewsets.ModelViewSet):
    queryset = actividades.objects.all().select_related("empleado")
    serializer_class = actividadesSerializer


class registroProyectoView(viewsets.ModelViewSet):
    queryset = RegistroProyecto.objects.all().select_related("trabaja")
    serializer_class = RegistroProyectoSerializer