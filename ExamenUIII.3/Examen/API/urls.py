from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empleados',views.empleadosView)
router.register('actividades',views.actividadesView)
router.register('registroProyecto',views.registroProyectoView)

urlpatterns = [
    path('',include(router.urls))
]
