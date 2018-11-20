from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, generics, permissions
from .Serializers import ProductosSerializer, PersonalSerializer,LineaProduccionSerializer,EntregaSerializer,AlmacenSerializer,OrdenesSerializer
from App.models import Productos, Personal, LineaProduccion,Entrega,Almacen, ordenes


class productoView(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class personalView(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class lineaProduccionView(viewsets.ModelViewSet):
    queryset = LineaProduccion.objects.all()
    serializer_class = LineaProduccionSerializer

class entregaView(viewsets.ModelViewSet):
    queryset = Entrega.objects.all().select_related("entrega", "recibe")
    serializer_class = EntregaSerializer

class almacenView(viewsets.ModelViewSet):
    queryset = Almacen.objects.all().select_related("entregas")
    serializer_class = AlmacenSerializer

class ordenesView(viewsets.ModelViewSet):
    queryset = ordenes.objects.all()
    serializer_class = OrdenesSerializer