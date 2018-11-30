from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('sche/', views.scheduler, name='scheduler'),
    path('editCalendar', views.editCalendar, name = 'editCalendar'),
    path('altaProyecto/',views.altaProyecto, name = 'altaProyecto'),
    path('consulta/', views.consulta, name = 'consulta'),
]