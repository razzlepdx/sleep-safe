from flask import Flask, request, redirect, render_template, flash, url_for, json, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# from flask_googlemaps import GoogleMaps
# from models.user import User
import os

# app and db dev environment settings:
######################################
db_uri = 'mysql+pymysql://sleep-safe:sleep-safe@localhost:3306/sleep-safe'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ZAj08N/$3m]XHjHy!rX R/~?X,9RW@UL'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


# runs the app, always the last line
if __name__ == '__main__':
    app.run(threaded = True)