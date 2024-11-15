from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    model = Student
    fields = ['name','student_email','locker_number']
    
class StudentAllSerializer(serializers.ModelSerializer):
    model = Student
    fields = [
        'name','student_email','personal_email',
        'locker_number','locker_combination','good_student'
              ]