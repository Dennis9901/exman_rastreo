from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración del esquema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Examen Rastreo",
        default_version='v1',
        description="Documentación automática con Swagger y Redoc",
        contact=openapi.Contact(email="tu.email@ejemplo.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vehiculos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('vehiculos.urls')),

    # Swagger / Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]