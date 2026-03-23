from django.contrib import admin
# AGREGA 'include' en la siguiente línea:
from django.urls import path, include 

from rest_framework.routers import DefaultRouter
from .views import CareerViewSet, DatasetViewSet

# Configuración del Router
router = DefaultRouter()
router.register(r'careers', CareerViewSet, basename='career')
router.register(r'datasets', DatasetViewSet, basename='dataset')
# Vistas para el Login (JWT)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints de Autenticación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoints del CRUD
    # Aquí es donde fallaba porque no encontraba 'include'
    path('api/', include(router.urls)), 
    
]