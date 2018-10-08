from django.shortcuts import render
from .models import seat,Palco,Fanatics
from .forms import SearchPalco,SearchFanDate
# Create your views here.
def home(request):
    return render(request,'ExamenTemplates/home.html')

def fanatics(request):
    fanatics = Fanatics.objects.all()
    return render(request,'ExamenTemplates/fanatics.html',{"fanatics":fanatics})

def fanaticsDetail(request,id):
    fanatics = Fanatics.objects.get(id=id)
    return render(request,'ExamenTemplates/fanaticsDetail.html',{"fanatics":fanatics})

def fanaticsDates(request):
     if request.method == 'POST':
        form = SearchFanDate(request.POST)
        if form.is_valid():
           inicio =  form.cleaned_data['inicio']    
           final = form.cleaned_data['final']
           fanatics = SearchFanDate.objects.filter(created__range(inicio,final))
     else:
        form = SearchFanDate()
        fanatics=None
     return render(request,'ExamenTemplates/fanaticsDates.html',{"form":form,"fanatics":fanatics})

def reports(request):
    fanatics = Fanatics.objects.all()
    return render(request,'ExamenTemplates/reports.html',{"fanatics":fanatics})

def palcos(request):
    palco = Palco.objects.all()
    return render(request,'ExamenTemplates/palcos.html',{"palco":palco})

def palcosSearch(request):
     if request.method == 'POST':
         form = SearchPalco(request.POST)
         
         if form.is_valid(): 
             NamePalco = form.cleaned_data('palco')
             palcos = Palco.objects.filter(palcoName=NamePalco)        
     else:
        form=SearchPalco()
        palcos=None
     return render(request,'ExamenTemplates/palcosSearch.html',{"form": form,"palcos":palcos})

def palcoFanatics(request):
    fanatics = Fanatics.objects.exclude(palco__isnull=True)
    return render(request,'ExamenTemplates/PalcoFanatic.html',{"fanatics":fanatics})

def Seat(request):
    seats = seat.objects.all()
    return render(request,'ExamenTemplates/seat.html',{"seats":seats})

def seatOrderCategories(request):
    seats = seat.objects.order_by('Category')
    return render(request,'ExamenTemplates/seatOrderCategories.html',{"seats":seats})