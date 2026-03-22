from rest_framework import viewsets, permissions
from .models import Career
from .serializers import CareerSerializer

class CareerViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona las acciones CRUD (List, Create, Retrieve, Update, Delete)
    para la tabla Career.
    """
    # 1. Definimos qué datos queremos mostrar y cómo ordenarlos
    queryset = Career.objects.all().order_by('-created_at')
    
    # 2. Le decimos qué serializador usar
    serializer_class = CareerSerializer
    
    # 3. Restringimos el acceso: Solo usuarios con Token JWT válido
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Este método se ejecuta justo antes de guardar en la base de datos.
        Extraemos el usuario del Token (request.user) y lo asignamos al campo 'user'.
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Opcional: Si quieres que cada usuario SOLO vea sus propias carreras,
        descomenta la línea de abajo. Si es un sistema compartido, déjalo así.
        """
        # return Career.objects.filter(user=self.request.user).order_by('-created_at')
        return super().get_queryset()