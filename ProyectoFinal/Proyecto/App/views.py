from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import forms as form_model, models as models_App


def index(request):
    return render(request,'index.html')

def scheduler(request):
    return render(request,'scheduler.html')

def editCalendar(request):
    return render(request, 'editarCalendario.html')

def altaProyecto(request):
    forma = form_model.RegistroProyecto(request.POST or None)
    if forma.is_valid():
        proyecto = forma.save(commit = False)
        return redirect('/')   
    else:
        print('algo')
        forma = form_model.RegistroProyecto()

    return render(request,'altaProyecto.html', {"forma": forma})

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
