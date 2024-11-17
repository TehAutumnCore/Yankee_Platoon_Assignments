from django.db import models
from django.core import validators as v
from subject_app.models import Subject
from student_app.models import Student

# Create your models here.
class Grade(model.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2,blank=False, default=100, validators=[v.MinValueValidator(0.00), v.MaxValueValidator(100.00)])
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_grades")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_grades")
    
    def __str__(self):
        return f"{self.Grade} - {self.a_subject} - {self.student}"