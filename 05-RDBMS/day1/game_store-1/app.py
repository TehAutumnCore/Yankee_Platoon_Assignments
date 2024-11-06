from flask import flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("server")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql + psycopg://desktop@localhost/game_store'
db.SQLAlchemy(app)

class Employees(db.model):
    id = db.column(db.Integer, primary_key=True)
    employee_name = db.column(db.String(50))
    position = db.column(db.String(50))
    salary=db.column(db.decimal(7,2))

class Posters(db.model):
    id = db.column(db.Integer, primary_key=True)
    postertitle = db.column(db.String(50))
    quantity = db.column(db.Integer)
    price = db.column(db.decimal(4,2))

class Action_Figures(db.model):
    id = db.column(db.Integer, primary_key=True)
    action_figures_title = db.column(db.String(50))
    quantity = db.column(db.Integer)
    price = db.column(db.decimal(4,2))

class Posters(db.model):
    game_id = db.column(db.Integer, primary_key=True)
    game_title = db.column(db.String(50))
    quantity = db.column(db.Integer)
    price = db.column(db.decimal(4,2))
    
app.run(debug=True, port=8000)