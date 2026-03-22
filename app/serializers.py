from rest_framework import serializers
from .models import Career
from .models import Dataset

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class DatasetSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True) # Campo virtual para el archivo

    class Meta:
        model = Dataset
        fields = ['id', 'name', 'description', 'type', 'file', 'created_at']
        read_only_fields = ['created_at']