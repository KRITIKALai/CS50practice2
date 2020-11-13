from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    name = "Aakash"
    now = datetime.datetime.now()
    isnewyear = now.month == 1 and now.day == 1
    return render_template("index.html", headline=name, isnewyear=isnewyear)

@app.route("/more")
def end():
    name = "Dhal"
    now = datetime.datetime.now()
    isnewyear = now.month == 1 and now.day == 1
    isnewyear = True
    return render_template("more.html", headline=name, isnewyear=isnewyear)
