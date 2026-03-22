import csv
import io
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Career
from .serializers import CareerSerializer
from .models import Dataset
from .serializers import DatasetSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    # Solo usuarios autenticados pueden usar este CRUD
    permission_classes = [permissions.IsAuthenticated]

    # Opcional: Para que al crear se guarde automáticamente el ID del usuario logueado
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # 1. Obtener el archivo y el tipo
        file = request.FILES.get('file')
        dataset_type = serializer.validated_data.get('type')
        
        # 2. Guardar el registro en la tabla 'datasets'
        dataset_obj = serializer.save(user=self.request.user, state=True)

        # 3. Procesar el CSV
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        if dataset_type == 'student':
            self.process_students(reader)
        elif dataset_type == 'record':
            self.process_records(reader)

        return Response(serializer.data, status=status.CREATED)

    def process_students(self, reader):
        # Aquí importarías tu modelo Student
        # from .models import Student
        # Por ahora un ejemplo de cómo iterar:
        for row in reader:
            # Student.objects.create(name=row['nombre'], ...)
            pass

    def process_records(self, reader):
        # Aquí importarías tu modelo AcademicRecord
        for row in reader:
            # AcademicRecord.objects.create(...)
            pass