from django.shortcuts import render,redirect
from .forms import Criticas
from .models import Critica

def home(request):
    return render(request,'home.html')

def critica(request):
    form = Criticas(request.POST or None)
    if form.is_valid():
        critica = form.save(commit=False)
        critica.files = 'none'
        critica.ranking = 0
        critica.save()
        return redirect('/criticas')
    else:
        form=Criticas()
    return render(request,'criticas.html',{'form':form})


def allCriticas(request):
    criticas =  Critica.objects.all()
    return render(request,'allCriticas.html',{'criticas':criticas})

def detalleCritica(request,id):
    criticas = Critica.objects.get(id=id)
    return render(request,'detalleCritica.html',{"criticas":criticas})
