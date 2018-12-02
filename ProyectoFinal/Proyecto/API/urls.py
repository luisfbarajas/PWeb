from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('empleado',views.empleadoView)
router.register('actividades',views.actividadesView)
router.register('RegistroProyecto',views.RegistroProyectoView)


urlpatterns = [
    path('', include(router.urls)),
]