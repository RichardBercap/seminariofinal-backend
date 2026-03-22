from rest_framework import viewsets, permissions
from .models import Career  # Importación relativa limpia
from .serializers import CareerSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all().order_by('-created_at')
    serializer_class = CareerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)