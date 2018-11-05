from django.shortcuts import render, redirect
from .forms import RegistroProyectos
from .models import empleados, RegistroProyecto, actividades


def home(request):
    form = RegistroProyectos(request.POST or None)
    if form.is_valid():
        proyecto = form.save(commit=False)
        proyecto.save()
        return redirect('/')
    else:
        form=RegistroProyectos()

    return render(request,'home.html',{"form":form})

def empleadoss(request):
    emple = empleados.objects.all()
    return render(request,'empleados.html',{"emple":emple})

def reunion(request):
    reunione = RegistroProyecto.objects.all()
    return render(request,'Reuniones.html',{"reunione":reunione})

def empleadoProyecto(request):
    relacionempleado =  RegistroProyecto.objects.all().select_related("trabaja")
    return render(request,'empeladoProyecto.html',{'relacionempleado':relacionempleado})

def actividadEmpleado(request):
    actividade = actividades.objects.all().select_related("empleado")
    return render(request,'actividadEmpleado.html',{"actividade":actividade})