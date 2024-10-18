import csv 
import os.path
from classes.person import Person

class Student(Person):

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id
    
    def __str__(self):
        return f'\n{self.name.upper()}\n---------------\nage: {self.age}\nid: {self.school_id}\n'

    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**dict(row)))

    def capture_id():
        id_list = [int(x.school_id) for x in self.students]
        new_id = max(id_list) + 1
        return new_id
    # @classmethod
    
    # new_student = {
    #     "name": input("Enter a student name: \n")
    #     "age": capture_age()
    #     "role": "Student"
    #     "school_id": capture_id()
    #     "password": input("Enter a student password \n")
    # }
    # 
    # return students
