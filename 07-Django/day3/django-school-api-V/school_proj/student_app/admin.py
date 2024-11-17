from django.contrib import admin
from .models import Student
from subject_app.models import Subject
from student_app.models import Student

# Register your models here.
admin.site.register([Student, Subject, Grade])