from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import json

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
    return jsonify (Club.query.all())

@app.route('/api/<username>')
def find_user (username):
    return jsonify (Users.query.filter_by(first_name=username).first ())
@app.route ('/api/<club_name>')
def find_club (club_name):
    return jsonify (Club.query.filter(Club.name.contains ('club_name')))

@app.route ("/api/add_club", methods=["POST","GET"])
def add_club ():
    if request.method == "POST":
        user=request.form ["nm"]
        return redirect (url_for("clubs"),usr=user)
    else:
        return render_template ("add_club.html")


if __name__ == '__main__':
    app.run()
