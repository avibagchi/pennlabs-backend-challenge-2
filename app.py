from flask import Flask, request, jsonify, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
import json

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.secret_key = 'PennLabs'
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
def clubs():
    data=[]
    count=0
    tag_arr = [] #only used if you uncomment below
    for x in range (len (Club.query.all())):
        data.append ({})

    for club_obj in Club.query.all():
        data[count]['name'] = club_obj.name
        json_data = json.dumps(data)
        count += 1
    return render_template("clubs.html", data=json_data)
    #Uncomment below if you want other attributes displayed:
    #data [x] ['code']=club_obj.code
    #data [x] ['description'] = club_obj.description
    #for tag_obj in Tags.query.filter_by (club=club_obj):
        #tag_arr.append (tag_obj.tag)
    #data [x]['tags']=tag_arr

@app.route('/api/finduser', methods = ['POST', 'GET'])
def find_user():
    if request.method == "POST":
        user = Users.query.filter_by(first_name=request.form.get("fname")).first()
        return "First Name: " + str(user.first_name) + "School: " + \
               str(user.school) + "Major: "+str (user.major)
    return render_template("find_user.html")

@app.route ('/api/findclub', methods = ['POST', 'GET'])
def find_club():
    arr=[]
    if request.method=="POST":
        club_list = Club.query
        club_list = club_list.filter (Club.name.like ("%" + request.form.get ("cname") + "%")).all()
        for club in club_list:
            arr.append("Code: " + str (club.code) + "Name: " + \
                        str (club.name) + "Description: " + str (club.description) + \
                        "Favorite Counter: "+str (club.fav_counter))
        return " ".join(arr)
    return render_template("find_club.html")

@app.route ("/api/addclub", methods=["POST","GET"])
def add_club ():
    if request.method == "POST":
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

@app.route ("/login/", methods=["POST","GET"])
def login ():
    if request.method=="POST":
        name = request.form.get ("fname")
        #username=name.lower ()
        print (name)
        session ['name']=name

        user = Users.query.filter_by(first_name=name).first()

        if user != None:
            return redirect("/favclub/")
        else:
            return "Invalid Credentials"

    return render_template("login.html")

#@app.route('/api/favclub', defaults={'id': None}, methods=["POST","GET"])
@app.route ("/favclub/", methods=["POST","GET"])
def fav_club ():
    name = request.args['name']
    name = session['name']
    if request.method == "POST":
        club = Club.query.filter_by(code=request.form.get ("fccode")).first ()
        club.fav_counter += 1
        user = Users.query.filter_by(first_name=name).first()
        print (user)
        fav = Favorites(favorite=club, users=user)
        db.session.commit()
        return "Added Favorite!"
    return render_template("favorites.html")

@app.route ("/api/modifyclub", methods=["POST","GET"])
def modify_club ():
    if request.method == "POST":
        club = Club.query.filter_by (code=request.form.get("cc").first ())
        tag_list = []
        tag_list.append (request.form.get("ct1"))
        tag_list.append (request.form.get("ct2"))
        tag_list.append (request.form.get("ct3"))

        for tag_str in tag_list:
            t = Tags.query.filter_by (tag=tag_str, club=club).first()
            t.tag=tag_str

        db.session.commit()
        return str(request.form.get("cc")) + " tags modified!"
    return render_template("modify_club.html")

@app.route ("/api/filter", methods=["POST","GET"])
def filter ():
    s= ""
    clubs = Club.query.all ()
    for club in clubs:
        s + str (Tags.query.filter_by(club=club).first().tag) +"\n"
    return render_template("filter.html", s=s)

@app.route ("/signup", methods=["POST","GET"])
def signup ():
    if request.method == "POST":
        user = Users(first_name=request.form.get("fn"), last_name=request.form.get("ln"),
                     grade=request.form.get("gr"), school=request.form.get("s"),
                     gender=request.form.get("ge"), major=request.form.get("m"))
        i1 = Interests(interest=request.form.get("i1"), users=user)
        i2 = Interests(interest=request.form.get("i2"), users=user)
        i3 = Interests(interest=request.form.get("i3"), users=user)

        f1 = Favorites(favorite=request.form.get("f1"), users=user)
        f2 = Favorites(favorite=request.form.get("f2"), users=user)
        f3 = Favorites(favorite=request.form.get("f3"), users=user)

        db.session.add_all([user])
        db.session.add_all([i1, i2, i3])
        db.session.add_all([f1, f2, f3])
        db.session.commit()

        return "<p> User Added! </p>"

    return render_template("signup.html")

if __name__ == '__main__':
    app.run()
