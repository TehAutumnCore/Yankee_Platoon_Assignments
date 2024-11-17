from django.db import models
from django.core import validators as v
from .validators import validate_subject_name, validate_professor_name
from student_app.models import Student

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(blank=False, unique=True, validators=[validate_subject_name])
    professor = models.CharField(blank=False, default="Mr. Cahan", validators=[validate_professor_name])

    def __str__(self):
        return f"{self.subject_name} - {self.professor}"