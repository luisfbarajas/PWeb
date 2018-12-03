from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import  models as models_App
from .forms import RegistroProyecto, addActivitiForm


def index(request):
    return render(request,'index.html')

def scheduler(request):
    return render(request,'scheduler.html')

def editCalendar(request):
    return render(request, 'editarCalendario.html')

def altaProyecto(request):
    forma = RegistroProyecto(request.POST)
    actividades = models_App.Actividades.objects.all()
    if forma.is_valid():
        proyecto = forma.save(commit = False)
        proyecto.userRegistro = request.user
        proyecto.save()
        return redirect('altaProyecto')   
    else:
        forma = RegistroProyecto()

    return render(request,'altaProyecto.html', {"forma": forma,"actividades":actividades})

def consulta(request):
    proyectos = models_App.RegistroProyecto.objects.all()
    return render(request,'Consulta.html', {'proyectos':proyectos})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def addActiviti(request):
    forma = addActivitiForm(request.POST)
    if forma.is_valid():
        actividad = forma.save(commit = False)
        actividad.save()
        return redirect('AddActiviti')
    else:
        forma = addActivitiForm()
    return render(request,'AddActiviti.html',{'forma':forma})