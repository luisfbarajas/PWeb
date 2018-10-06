from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'ExamenTemplates/home.html')

def fanatics(request):
    return render(request,'ExamenTemplates/fanatics.html')

def fanaticsDetail(request):
    return render(request,'ExamenTemplates/fanaticsDetail.html')

def fanaticsDates(request):
    return render(request,'ExamenTemplates/fanaticsDates.html')

def reports(request):
    return render(request,'ExamenTemplates/reports.html')

def palcos(request):
    return render(request,'ExamenTemplates/palcos.html')

def palcosSearch(request):
    return render(request,'ExamenTemplates/palcosSearch.html')

def palcoFanatics(request):
    return render(request,'ExamenTemplates/PalcoFanatic.html')

def seat(request):
    return render(request,'ExamenTemplates/seat.html')

def seatOrderCategories(request):
    return render(request,'ExamenTemplates/seatOrderCategories.html')