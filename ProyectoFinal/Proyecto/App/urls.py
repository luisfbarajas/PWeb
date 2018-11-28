from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name = 'logout'),
    path('signup/', views.signup, name = 'signup')
]