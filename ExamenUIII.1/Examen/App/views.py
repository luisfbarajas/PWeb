from django.shortcuts import render
from .models import Almacen,Personal,Productos, LineaProduccion,Entrega,ordenes


def home(request):
    return render(request,'home.html')

def almacen(request):
    almacen  = Almacen.objects.all()
    return render(request,'Almacen.html',{"almacen":almacen})

def lineasProduccion(request):
    # lineas = LineaProduccion.objects.all().select_related("trabaja")
    return render(request,'lineasProduccion.html')

def solicitarMaterial(request):
    return render(request,'solicitarMaterial.html')

def personalArea(request):
    personal = Personal.objects.all().order_by("linea")
    return render(request,'PersonalArea.html',{"personal":personal})

def entregas(request):
    entregas =  Entrega.objects.all().order_by('fecha')
    return render(request,'Entregas.html',{"entregas":entregas})

def revisados(request):
    producto = Productos.objects.all()
    return render(request,'revisados.html',{"producto": producto})

def orden(request):
    Ordenes = ordenes.objects.all().order_by('fecha')
    return render(request,'ordenes.html',{"Ordenes":Ordenes})

def productoorden(request):
    producto = Productos.objects.all().order_by('fecha')
    return render(request,'productosorder.html',{"producto":producto})