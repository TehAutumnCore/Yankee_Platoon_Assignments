from flask import flask
from SQLAlchemy import sqlalchemy

app = flask("Server")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql + psycopg://desktop@localhost/school'

db = SQLAlchemy(app)

#DB named School

class Students(db.model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.Integer)

class Subjects(db.model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(50))
    
class Teachers(db.model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

students = [
    # id,first_name,last_name,age,subject -> students.csv
    {'id': '1','first_name':'David','last_name':'Miller','age':32,'subject':3},
    {'id': '2','first_name':'Sarah','last_name':'Johnson','age':28,'subject':1},
    {'id': '3','first_name':'Robert','last_name':'Williams','age':35,'subject':4},
    {'id': '4','first_name':'Emily','last_name':'Anderson','age':30,'subject':5},
    {'id': '5','first_name':'Michael','last_name':'Smith','age':29,'subject':4},
    {'id': '6','first_name':'Olivia','last_name':'Johnson','age':31,'subject':5},
    {'id': '7','first_name':'Matthew','last_name':'Brown','age':27,'subject':3},
    {'id': '8','first_name':'John','last_name':'Doe','age':29,'subject':1},
    {'id': '9','first_name':'Laura','last_name':'Clark','age':30,'subject':2},
    {'id': '10','first_name':'Rebecca','last_name':'Wilson','age':33,'subject':2},
    {'id': '11','first_name':'Chris','last_name':'Evans','age':31,'subject':1},
    {'id': '12','first_name':'Anna','last_name':'Robinson','age':29,'subject':1},
    {'id': '13','first_name':'James','last_name':'Moore','age':34,'subject':5},
    {'id': '14','first_name':'Elizabeth','last_name':'White','age':28,'subject':3},
    {'id': '15','first_name':'William','last_name':'Harris','age':30,'subject':5},
    {'id': '16','first_name':'Julia','last_name':'Lewis','age':32,'subject':4},
    {'id': '17','first_name':'Daniel','last_name':'Turner','age':29,'subject':3},
    {'id': '18','first_name':'Grace','last_name':'Parker','age':35,'subject':4},
    {'id': '19','first_name':'Charles','last_name':'Bennett','age':28,'subject':2},
    {'id': '20','first_name':'Sophia','last_name':'Wright','age':30,'subject':1}
]

subjects = [
    # id,subject -> subjects.csv
    {'id':'1','subject':'Mathematics'},
    {'id':'2','subject':'Science'},
    {'id':'3','subject':'English'},
    {'id':'4','subject':'History'},
    {'id':'5','subject':'Physical Education'}
]

teachers = [
    # id,first_name,last_name,age,subject       -> teachers.csv
    {'id':'1','first_name':'David','last_name':'Miller','age':32,'subject':1},
    {'id':'2','first_name':'Sarah','last_name':'Johnson','age':28,'subject':2},
    {'id':'3','first_name':'Robert','last_name':'Williams','age':35,'subject':3},
    {'id':'4','first_name':'Emily','last_name':'Anderson','age':30,'subject':4},
    {'id':'5','first_name':'Michael','last_name':'Smith','age':29,'subject':5}
]

#Endpoints

#/students
#   -Returns a list of students along with their class names and the teacher of their class
#   -the response shouold be in json format, following the structure of the readme

@app.route("/students_classes_teachers",methods=['GET'])
def students_classes_teachers():
    pass
    

#/teachers
#   -Returns an array of teachers, the subjects they teach, and the students within each subject
#   -The reponse should be in json format, followin ghte structure of the readme

@app.route("/teachers_subjects_their_students",methods=['GET'])
def teachers_subjects_their_students():
    pass
    
#/Subjects
#   -Return a list of subject dictionaries with the students enrolled in each class and the teacher who teaches each subject
#   -Please provide an example of the response structure for this endpoint

@app.route("/students_each_class_teacher_each_subject",methods=['GET'])
def students_each_class_teacher_each_subject():
    pass

app.run(debug=True,port=8000)