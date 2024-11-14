from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, blank=False)
    student_email = models.EmailField(unique=True, blank=False)
    personal_email = models.EmailField(unique=True)
    locker_number = models.IntegerField(blank=False, unique=True, default=110)
    locker_combination = models.CharField(max_length=8,blank=False, default="12-12-12")
    good_student = models.BooleanField(default=True, blank=False)
    
    def __str__(self):
        return f"Name: {self.name} Stud Email:{self.student_email} Locker #:{self.locker_numer} Good Student: {good_student}"
