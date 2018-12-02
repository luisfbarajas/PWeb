from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, generics, permissions
from App.models import empleados, Actividades,RegistroProyecto
from .Serializers import empeladosSerializer,ActividadesSerializer,RegistroProyectoSerializer


class empleadoView(viewsets.ModelViewSet):
    queryset = empleados.objects.all()
    serializer_class = empeladosSerializer

class actividadesView(viewsets.ModelViewSet):
    queryset = Actividades.objects.all()
    serializer_class = ActividadesSerializer

class RegistroProyectoView(viewsets.ModelViewSet):
    queryset = RegistroProyecto.objects.all()
    serializer_class = RegistroProyectoSerializer
