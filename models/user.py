from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(20))
    comments = db.relationship('Comment', backref='user')

def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

def __repr__(self):
    return '<User %r>' % self.name