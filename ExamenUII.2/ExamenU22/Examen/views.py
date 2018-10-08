from django.shortcuts import render
from .models import Personal, Activities

# Create your views here.
def home(requets):
    return render(requets,'home.html')

def reports(requets):
    personal = Personal.objects.all()
    return render(requets,'reports.html',{"personal":personal})

def personal(requets):
    personal = Personal.objects.order_by('activitie')
    return render(requets,'personal.html',{"personal":personal})

def activities(requets):
    activities=Activities.objects.all()
    return render(requets,'activities.html',{"activities":activities})