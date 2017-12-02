from app import db, datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    comment = db.relationship('Comment', backref='user')

def __init__(self, user_id, rating, comment):
    self.user_id = user_id
    self.rating = rating
    self.timestamp = datetime.now()
    self.comment = comment

def __repr__(self):
    return '<User %r>' % self.name