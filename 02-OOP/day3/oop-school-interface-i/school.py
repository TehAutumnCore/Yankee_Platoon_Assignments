from classes.staff import Staff
from classes.students import Student
class School:
    
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()