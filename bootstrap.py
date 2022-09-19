import os
from app import db, DB_FILE
from app import Users, Interests, Favorites
import json

def create_user():

    josh = Users (first_name="josh", last_name="Smith", grade="Freshman",
                  school="CAS", gender="Male", major="Computer Science")
    i1 = Interests(interest="baseball", users=josh)
    i2 = Interests(interest="computer science", users=josh)
    i3 = Interests(interest="quant", users=josh)

    tony = Users (first_name="tony", last_name="Harris", grade="Freshman",
                  school="CAS", gender="Male", major="History")
    i4 = Interests(interest="history", users=tony)
    i5 = Interests(interest="quant", users=tony)
    i6 = Interests(interest="basketball", users=tony)

    jeff = Users(first_name="jeff", last_name="Brown", grade="Freshman",
                 school="CAS", gender="Male", major="History")
    i7 = Interests(interest="history", users=jeff)
    i8 = Interests(interest="quant", users=jeff)
    i9 = Interests(interest="basketball", users=jeff)

    f1 = Favorites (favorite="pppjo", users=jeff)
    f2 = Favorites (favorite="lorem-ipsum", users=jeff)

    avi = Users(first_name="avi", last_name="Bagchi", grade="Freshman",
                 school="CAS", gender="Male", major="CS")
    i7 = Interests(interest="baseball", users=jeff)
    i8 = Interests(interest="quant", users=jeff)
    i9 = Interests(interest="basketball", users=jeff)

    f1 = Favorites (favorite="pppjo", users=jeff)
    f2 = Favorites (favorite="lorem-ipsum", users=jeff)



    db.session.add_all ([josh, tony, jeff])
    db.session.add_all ([i1,i2,i3,i4,i5,i6,i7,i8,i9])
    db.session.add_all([f1, f2])
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

        club = Club (code=data[x]['code'], name=data[x]['name'],
                     description=data[x]['description'], fav_counter=0)

        db.session.add(club)

        for tag_str in data[x]['tags']:
            t = Tags(tag=tag_str, club=club)
            db.session.add(t)

        db.session.commit()

# No need to modify the below code.
if __name__ == '__main__':
    # Delete any existing database before bootstrapping a new one.
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    db.create_all()
    create_user()
    load_data()
