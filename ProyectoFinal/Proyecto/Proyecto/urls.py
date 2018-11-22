from django.contrib import admin
from django.urls import path, include
from App import views
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
    path('api',include('API.urls')),
]
