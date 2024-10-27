from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("Server")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql + psycopg://desktop@localhost/school'

db = SQLAlchemy(app)

class Student(db.model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    
class Subject(db.model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(50))
    
class Teacher(db.model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]



@app.route("/", methods=['GET'])
def home():
    return """
<h1> Yankee Student Portal</h1>
<h5><a href ='/old_students/'>Old Students</h5>
<h5><a href ='/young_students/'>Young Students</h5>
<h5><a href ='/advance_students/'>Advance_students</h5>
<h5><a href ='/student_names/'>Students Names</h5>
<h5><a href ='/student_ages/'>Students Ages</h5>
<h5><a href ='/students/'>All Students</h5>
"""

@app.route("/old_students/",methods=['GET'])
def old_students(): #Returns an array of student objects where the students are older than 20 years old
    # old_students = []
    # for student in students:
    #     if student['age'] > 20:
    #         old_students.append(student)
    # return jsonify(old_students)

    old_students = [student for student in students if student['age'] > 20]
    # old_students = [student for student in students if student['age'] > 20 and student['age'] < 22 ]
    return jsonify(old_students)

@app.route("/young_students/",methods=['GET']) 
def young_students():#Returns an array of student objects where the students are younger than 21 years old
    # young_students = []
    # for student in students:
    #     if student['age'] < 21:
    #         young_students.append(student)
    # return jsonify(young_students)

    young_students = [student for student in students if student['age'] < 21]
    return jsonify(young_students)
    
@app.route("/advance_students/",methods=['GET'])
def advance_students():#Returns an array of student objects where the students are younger than 21 and have a letter grade of "A
    # advance_students = []
    # for student in students:
    #     if student['age'] < 21 and student['grade'] == 'A':
    #         advance_students.append(student)
    # return jsonify(advance_students)

    advance_students = [student for student in students if student['age'] < 21 and student['grade'] == 'A']
    return jsonify(advance_students)
    
@app.route("/student_names/",methods=['GET'])
def student_names(): #Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values
    # student_names = []
    # for student in students:
    #     student_names.append({
    #         'id': student['id'],
    #         'first_name': student['first_name'],
    #         'last_name': student['last_name']
    #     })
    # return jsonify(student_names)
    student_names = [
    {   'id': student['id'],
        'first_name': student['first_name'],
        'last_name': student['last_name']
    }for student in students]
    return jsonify(student_names)
    
#     @app.route("/student_names/", methods=["GET"])
# def get_student_names():
#     student_names = list(map(lambda student: f"{student["first_name"]} {student["last_name"]}", students))
#     return jsonify(student_names)
    
    
@app.route("/student_ages/",methods=['GET'])
def student_ages():#Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
    student_ages = [
    {'first_name': student['first_name'],
    'last_name': student['last_name'],
    'age': student['age']
    }for student in students]
    return jsonify(student_ages)

@app.route("/students/",methods=['GET'])
def get_students():#Returns an array of all student objects available.
    student = []
    for student in students:
        return jsonify(students)
#  "<h5><a href ='localhost:8000/students/>' students>All Students</h5>"

app.run(debug=True,port = 8000)