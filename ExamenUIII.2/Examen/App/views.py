from django.shortcuts import render
from .forms import Criticas

def home(request):
    return render(request,'home.html')

def critica(request):
    form = Criticas
    return render(request,'criticas.html',{'form':form})


def allCriticas(request):
    return render(request,'allCriticas.html')
