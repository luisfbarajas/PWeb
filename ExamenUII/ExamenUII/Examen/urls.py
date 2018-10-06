from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fanatics/',views.fanatics, name='fanatics'),
    path('fanaticsDetail/',views.fanaticsDetail,name='fanaticsDetail'),
    path('fanaticsDates/',views.fanaticsDates,name='fanaticsDates'),
    path('reports/',views.reports,name='reports'),
    path('palcos/',views.palcos,name='palcos'),
    path('palcosSearch/',views.palcosSearch,name='palcosSearch'),
    path('PalcoFanatic/',views.palcoFanatics,name='palcoFanatic'),
    path('seat/',views.seat,name='seat'),
    path('seatOrderCategories/',views.seatOrderCategories,name='seatOrderCategories'),

]