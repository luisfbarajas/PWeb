from django.shortcuts import render

# Create your views here.
def home(requets):
    return render(requets,'home.html')

def reports(requets):
    return render(requets,'reports.html')

def personal(requets):
    return render(requets,'personal.html')

def activities(requets):
    return render(requets,'activities.html')