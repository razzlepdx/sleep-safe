from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db, bcrypt

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    # email = db.Column(db.String(40), unique=True)
    # password = db.Column(db.String(20))
    # comments = db.relationship('Comment', backref='user')
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    location_id = db.Column(db.Integer, ForeignKey('location.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return 'title: {}'.format(self.title)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    safe_score = db.Column(db.Integer, default=0)

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return 'name: {} '.format(self.name)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(20))
    comments = db.relationship('Comment', backref='user')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.name