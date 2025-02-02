from django.db import models
from django.core import validators as v
from .validators import (
    validate_combination_format,
    validate_name_format,
    validate_school_email,
)
from django.core.exception import ValidationError
from subject_app.models import Subject


# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_name_format]
    )
    student_email = models.EmailField(
        null=False, blank=False, unique=True, validators=[validate_school_email]
    )
    personal_email = models.EmailField(null=False, blank=False, unique=True)
    locker_number = models.IntegerField(
        default=110,
        null=False,
        blank=False,
        unique=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        default="12-12-12",
        null=False,
        blank=False,
        max_length=255,
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField(Subject, blank=False, validators=[v.MinLengthValidator(1), v.MaxLengthValidator(7)], related_name='students')

    def __str__(self):
        return f"{self.name} - {self.student_email}"
    
    def add_subject(self, subject_id):
        if self.subjects.count() < 7:
            self.subject.add(subject_id)
        else:
            raise Exception("This students class schedule is full!")
        
    def remove_subject(self, subject_id):
        if self.subject.count() > 1:
            self.subject.remove(subject_id)
        else:
            raise Exception("This student class schedule is empty!")