from rest_framework import serializers
from .models import Career  # Importación limpia gracias al __init__.py

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id', 'name', 'state', 'created_at', 'updated_at', 'user']
        # Protegemos campos que el usuario no debe manipular manualmente
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']