from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class chicken(db.Model):
    name = db.Column(db.String(20))
    time = db.Column(db.String(15))
    isReady = db.Column(db.Bool)

def __init__(self, name, time, isReady):
    self.name = name
    self.time = time
    self.isReady = isReady

db.create_all()

@app.route('/')
def show_all():
   return render_template('show_all.html', chickens = chicken.query.all() )