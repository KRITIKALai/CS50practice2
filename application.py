from flask import Flask,render_template,request,session
from flask_session import Session
import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"]=True
app.config["SESSION_TYPE"]="filesystem"
Session(app)

resolutions_ = []
nam = ""

@app.route("/")
def index():
    now = datetime.datetime.now()
    isnewyear = now.month == 1 and now.day == 1
    return render_template("index.html", isnewyear=isnewyear)

@app.route("/resolutions", methods= ["GET","POST"])
def resolutions():
    if session.get("resolutions_") is None:
        session["resolutions_"] = []
    if request.method == "POST":
        global nam
        if request.form.get("name"):
            nam = str(request.form.get("name"))
        resolution = request.form.get("resolution")
        session["resolutions_"].append(resolution)

    return render_template("resolutions.html", name=nam, resolutions = session["resolutions_"][1:]) #if resolutions_ else render_template("resolutions.html", name=nam)


    #if resolutions_:
    #    resolution = request.form.get("resolution")
    #    resolutions_.append(resolution)

    #    return render_template("resolutions.html", name=name, resolutions = resolutions_)



#if __name__ == "__main__":
#    app.run(debug=True)
