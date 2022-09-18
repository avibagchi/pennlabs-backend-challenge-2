from app import db

class Club (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String (50), nullable=False)
    name = db.Column (db.String (75), nullable=False)
    description = db.Column (db.String (250), nullable=False)

    tags_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
    tags = db.relationship ('Tags', backref=db.backref ('clubs',lazy=True))
    def __repr__(self):
        return '<Club %r>' % self.code
class Tags (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (50), nullable=False)
    def __repr__(self):
        return '<Tags %r>' % self.name


# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
