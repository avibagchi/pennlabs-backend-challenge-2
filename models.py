from app import db

class Club (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String (50), nullable=False)
    name = db.Column (db.String (75), nullable=False)
    description = db.Column (db.String (250), nullable=False)

    tags = db.relationship ('Tags', backref=db.backref ('club',lazy=True))
    def __repr__(self):
        return '<Club %r>' % self.code
class Tags (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    tag = db.Column(db.String (50), nullable=False)
    def __repr__(self):
        return '<Tags %r>' % self.tag

class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String (50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String (5), nullable=False)
    school = db.Column(db.String (50), nullable=False)
    gender = db.Column(db.String (10), nullable=False)
    major = db.Column(db.String (50), nullable=False)

    interests = db.relationship ('Interests', backref=db.backref ('users',lazy=True))

    def __repr__(self):
        return '<Users %r>' % self.first_name
class Interests (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    interest = db.Column(db.String (50), nullable=False)
    def __repr__(self):
        return '<Tags %r>' % self.interest


# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
