import csv
import io
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Career
from .serializers import CareerSerializer
from .models import Dataset,Student
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

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print("Datos recibidos:", request.data)
        
        dataset_type = request.data.get('type')
        data_content = request.data.get('content')

        if not isinstance(data_content, list):
            return Response({'error': 'content debe ser una lista'}, status=400)
        
        dataset_instance = None
        if len(data_content) > 0:
            dataset_serializer = DatasetSerializer(data={
                'name': request.data.get('name', 'Dataset sin nombre'),
                'description': request.data.get('description', ''),
                'type': dataset_type,
                'user': request.user.id,
                'state': True,
                'validation': False,
            })
            dataset_serializer.is_valid(raise_exception=True)
            dataset_instance = dataset_serializer.save()  #  guardar


        if dataset_type == 'Estudiantes':
            self.process_students(data_content, request, dataset_instance)
        elif dataset_type == 'Notas':
            self.process_records(data_content)

        return Response({'message': 'Carga exitosa'}, status=201)

    def process_students(self, data, request, dataset_instance):
        students = []

        for row in data:
            print("Fila:", row)

            try:
                career = Career.objects.get(id=row.get('id_career'))
            except Career.DoesNotExist:
                continue  # o manejar error

            student = Student(
                id_career=career,
                user=request.user,
                id_dataset=dataset_instance,
                who_pays=row.get('who_pays'),
                nationality=row.get('nationality'),
                marital_status=row.get('marital_status'),
                gender=row.get('gender'),
                age=int(row['age']) if row.get('age') else None,
                lastname=row.get('lastname'),
                name=row.get('name'),
                student_code=row.get('student_code'),
                state=True,
            )

            students.append(student)

        Student.objects.bulk_create(students)

    def process_records(self, reader):
        # modelo AcademicRecord
        for row in reader:
            
            pass