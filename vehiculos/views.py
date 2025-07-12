from rest_framework import viewsets, permissions
from .models import Vehiculo
from .serializers import VehiculoSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class VehiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Vehiculo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def mapa(request):
    return render(request, 'mapa.html')
