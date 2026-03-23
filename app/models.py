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
    type = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'datasets'


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)

    id_career = models.ForeignKey(
        Career,
        on_delete=models.RESTRICT,
        db_column='id_career',
        related_name='students'
    )

    id_dataset = models.ForeignKey(
        Dataset,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='id_dataset',
        related_name='students'
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    who_pays = models.CharField(max_length=100, null=True, blank=True)
    state = models.BooleanField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    lastname = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    student_code = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'student'  

    def __str__(self):
        return f"{self.name} {self.lastname}"