from app import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50), unique=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    safe_score = db.Column(db.Integer, default=0)

def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

def __repr__(self):
    return 'name: {} '.format(self.name)