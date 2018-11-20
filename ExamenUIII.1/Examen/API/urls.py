from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('personal',views.personalView)
router.register('lineaProduccion',views.lineaProduccionView)
router.register('almacen',views.almacenView)
router.register('productos',views.productoView)
router.register('entrega', views.entregaView)
router.register('ordenes',views.ordenesView)

urlpatterns = [
    path('',include(router.urls))
]
