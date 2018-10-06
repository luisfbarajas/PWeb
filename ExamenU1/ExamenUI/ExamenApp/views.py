from django.shortcuts import render
# from django.http import HttpResponse
from .models import Player, Stadium, Team
from .forms import PlayerForm, PlayerTeamForm


# Create your views here.
def home(request):
    return render(request, 'ExamenApp/home.html')

def teams(request):
    team = Team.objects.all()
    return render(request, 'ExamenApp/teams.html', {"teams": team})

def players(request):
    player = Player.objects.all().select_related("Id_Team")
    return render(request, 'ExamenApp/players.html', {"players":player,})

def stadium(request):
    stadiums = Stadium.objects.all().select_related("Id_Team")

    return render(request, 'ExamenApp/stadium.html', {"stadiums": stadiums})

def detail(request, id):
    player = Player.objects.get(id=id)
    return render(request,'ExamenApp/playerDetail.html', {"player":player})

def stadiumDetail(request,id):
    stadium = Stadium.objects.get(id=id)
    return render(request,'ExamenApp/stadiumDetail.html',{"stadium": stadium})

def teamDetail(request,id):
    team = Team.objects.get(id=id)
    return render(request,'ExamenApp/teamDetail.html',{'team':team})

def searchTeam(request):
    if request.method == 'POST':
        form = PlayerTeamForm(request.POST)
        if form.is_valid():

            position =  form.cleaned_data['team']
            # player = Player.objects.select_related("Id_Team").filter(Id_Team_NameTeam=position)
            player = Player.objects.filter(Id_Team__NameTeam__contains = position)

    else:
        form = PlayerTeamForm()
        player=''
    return render(request,'ExamenApp/searchTeam.html', {'form': form, 'players':player})

def searchPosition(request):
     if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
           position =  form.cleaned_data['position']    
           player = Player.objects.filter(position=position)
     else:
        form = PlayerForm()
        player=''
     return render(request,'ExamenApp/searchPosition.html', {'form': form, 'players':player})