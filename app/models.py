from django.db import models
from django.conf import settings

class Career(models.Model):
    name = models.CharField(max_length=100)
    state = models.BooleanField(default=True)
    # Asegúrate de que sean DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'career'

class Dataset(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    validation = models.BooleanField(default=False)
    state = models.BooleanField(default=True)
    type = models.CharField(max_length=30, null=True, blank=True) # 'student' o 'record'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'datasets'