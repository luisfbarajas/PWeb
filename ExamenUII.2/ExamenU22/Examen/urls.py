from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('activities/', views.activities, name='activities'),
    path('reports/',views.reports,name='reports'),
    path('personal/',views.personal,name='personal'),
]
