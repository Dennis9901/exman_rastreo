from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, mapa

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')

urlpatterns = [
    path('', include(router.urls)),
    path('mapa/', mapa, name='mapa')
]
