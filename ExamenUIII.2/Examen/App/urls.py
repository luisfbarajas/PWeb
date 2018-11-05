from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('criticas',views.critica, name='critica'),
    path('allCriticas',views.allCriticas, name='allCriticas'),
    path('detalleCritica/<int:id>', views.detalleCritica, name='detalleCritica'),
]