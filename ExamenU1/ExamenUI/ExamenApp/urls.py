from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.players),
    path('teams/', views.teams),
    path('stadium/', views.stadium),
    path('players/<int:id>', views.detail, name='detail'),
    path('stadium/<int:id>',views.stadiumDetail, name='detailStadium'),
    path('teams/<int:id>', views.teamDetail, name='detailTeam'),
    path('searchTeam/',views.searchTeam, name= 'searchTeam'),
    path('searchPosition/', views.searchPosition,name='searchPosition'),


]