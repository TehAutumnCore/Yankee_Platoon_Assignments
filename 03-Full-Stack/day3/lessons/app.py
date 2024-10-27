from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("server") #creating an instance of the flask object
#API: https://pokeapi.co/api/v2/pokemon/

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://desktop@localhost/school' #going into config(dictionary) and settings a keyvalue pair so sqlalchemy can find out db
# ="postgressqk"://desktop@localhost/school
# class name is name of table

db = SQLAlchemy(app) #looks into the flask server, looks for sql dictionary above in config, locates key and accesses it

class Student(db.model): #looks for the class and inherits for the db.model and converts it into a sql data table
    id = db.Column(db.Integer, primary_key = True) # id SERIAL PRIMARY KEY  #DATA MODEL that will represent the model of the object in SQL
    first_name = db.column(db.String(50)) #VARCHAR(50)
    last_name = db.column(db.String(50)) #VARCHAR(50)
    age = db.column(db.Integer) #age INT
    grade = db.column(db.String(1)) #CHAR(1)

students = [
#     id  first_name :firstname lastname:Lastname     age: age   grade:grade
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
]

# def get_students():
#     return students

@app.route("/students/",methods=['GET'])
def get_students():
    print(Student.query.all()) #SELECT * FROM student
    students = [{
        'id': stud.id,
        'first_name': stud.first_name,
        'last_name' : stud.last_name,
        'age':stud.age,
        'grade':stud.grade
    } for stud in students.query.all()] #querys db, grabs all the students in the dictionary, and returns it
    return jsonify(students) #take the list of dctionaries above, convert it into a json format and import it to the browser at port/students/

#psql
#INSERT INTO student VALUES (id,first_name,last_name,age,grade)
# 7,'adam','cahan',22,'A';


#127.0.0.1:8000/
@app.route("/",methods=['GET'])
def home():
    return "<h1> Yankee Student Portal</h1>"

#app.route(request,route,methods,func):
    #if request.method in methods:
        #return func

app.run(debug=True, port = 8000) #Settings the active port to 8000, default port is 5500 