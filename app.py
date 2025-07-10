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
    
def get_from_csv():
    Project.query.delete()
    
    with open("projects(Sheet1).csv", "r") as file:
        for row in csv.DictReader(file):
            project = Project(
                title=row["title"],
                description=row["description"],
                language=row["language"],
                link=row["link"]
            )
            db.session.add(project)
    db.session.commit()

with app.app_context():
    db.create_all()
    get_from_csv()
            
@app.route("/")
def index():
    projects=Project.query.all()
    return render_template("index.html", projects=projects)
