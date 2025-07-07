from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    db=sqlite3.connect("portfolio.db")
    cur=db.cursor()
    cur.execute("SELECT title, description, languages, link FROM projects")
    projects=cur.fetchall()
    db.close()
    return render_template("index.html", projects=projects)
