import os
from app import db, DB_FILE
from app import Users, Interests
import json

def create_user():
    i=Interests (interest=["baseball","quant","coding"])
    josh = Users (first_name="Josh", last_name="Smith", grade="Freshman",
                  school="CAS", gender="Male", major="Computer Science",interests=i)
    db.session.add(josh)
    db.session.commit ()
def load_data():
    from models import Club
    from models import Tags
    from models import Users
    from models import Interests

    json_file_path = "clubs.json"
    with open(json_file_path, 'r') as j:
        data = json.loads(j.read())

    for x in range(len(data)):
        t=Tags (tag=data[x]['tags'])
        club = Club (code=data[x]['code'], name=data[x]['name'],
                     description=data[x]['description'], tags=t)
        db.session.add(club)
        db.session.commit()


# No need to modify the below code.
if __name__ == '__main__':
    # Delete any existing database before bootstrapping a new one.
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    db.create_all()
    create_user()
    load_data()
