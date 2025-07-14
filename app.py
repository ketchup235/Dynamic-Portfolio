from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy 
import csv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Project(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description=db.Column(db.Text, nullable=False)
    language=db.Column(db.String(100), nullable=False)
    link=db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"<Project {self.title}>"

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio= db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<Person {self.name}>"

class Experience(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description=db.Column(db.Text, nullable=False)
    
def get_item_from_csv(filename, model_class, fields):
    model_class.query.delete()
    with open(filename, "r", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            item_data = {field: row[field] for field in fields}
            item = model_class(**item_data)
            db.session.add(item)
    db.session.commit()

with app.app_context():
    db.create_all()
    get_item_from_csv("projects(Sheet1).csv", Project, ["title", "description", "language", "link"])
    get_item_from_csv("person(Sheet1).csv", Person, ["name", "bio"])
    get_item_from_csv("exp.csv", Experience, ["title", "description"])
    
            
@app.route("/")
def index():
    person= Person.query.first()
    projects=Project.query.all()
    experience= Experience.query.all()
    return render_template("index.html", projects=projects, person=person, experience=experience)
