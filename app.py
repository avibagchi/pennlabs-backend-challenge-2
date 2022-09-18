from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import json2html

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *


@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})

@app.route('/api/clubs')
def clubs ():
    data=[]
    count=0
    tag_arr = []
    for x in range (len (Club.query.all())):
        data.append ({})

    for club_obj in Club.query.all():
        data [count] ['name']=club_obj.name
        json_data = json.dumps(data)
        count+=1
    return render_template("clubs.html", data=json_data)
    #Uncomment below if you want other attributes displayed:
    #data [x] ['code']=club_obj.code
    #data [x] ['description'] = club_obj.description
    #for tag_obj in Tags.query.filter_by (club=club_obj):
        #tag_arr.append (tag_obj.tag)
    #data [x]['tags']=tag_arr

@app.route('/api/finduser', methods = ['POST', 'GET'])
def find_user ():
    if request.method=="POST":
        user = Users.query.filter_by(first_name=request.form.get ("fname")).first ()
        return "First Name: " + str (user.first_name) + "School: "+ \
               str (user.school) + "Major: "+ str (user.major)
    return render_template("find_user.html")

@app.route ('/api/findclub', methods = ['POST', 'GET'])
def find_club ():
    arr=[]
    if request.method=="POST":
        club_list = Club.query
        club_list = club_list.filter (Club.name.like ("%" + request.form.get ("cname") + "%")).all()
        for club in club_list:
            arr.append ("Code: " + str (club.code) + "Name: "+ \
                   str (club.name) + "Description: " + str (club.description))
        return " ".join (arr)
    return render_template("find_club.html")

@app.route ("/api/addclub", methods=["POST","GET"])
def add_club ():
    if request.method == "POST":
        print ("WE ARE IN POST")
        club = Club(code=request.form.get("cc"), name=request.form.get("cn"),
                    description=request.form.get("cd"))
        db.session.add(club)
        tag_list = []
        tag_list.append (request.form.get("ct1"))
        tag_list.append (request.form.get("ct2"))
        tag_list.append (request.form.get("ct3"))

        for tag_str in tag_list:
            t = Tags(tag=tag_str, club=club)
            db.session.add(t)
        db.session.commit()
        return str(request.form.get("cn")) + " added!"
    return render_template("add_club.html")




if __name__ == '__main__':
    app.run()
