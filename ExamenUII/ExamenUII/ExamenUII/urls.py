from django.contrib import admin
from django.urls import path, include
from Examen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Examen.urls')),
]
