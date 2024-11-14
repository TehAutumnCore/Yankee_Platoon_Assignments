from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False,unique=True)
    personal_email = models.EmailField(null = True, blank = True, unique=True)
    locker_number = models.IntegerField(default=110, null = False, blank = False, unique=True)
    locker_combination = models.CharField(default="12-12-12",max_length=255, null = False, blank = False, unique=False)
    good_student = models.BooleanField(default=True, blank=False, unique=False)
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self,value: int):
        self.locker_number = value
        self.save()
    
    def student_status(self,value: bool):
        self.good_student = value
        self.save()