from flask import Flask, request, redirect, render_template, flash, url_for, json, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_googlemaps import GoogleMaps
from models.user import User
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

# routes:
# all routes get a decorator `@app.route` that takes at least one parameter - the url.  
# optional parameter: HTTP request types go here too.  if left blank it defaults to a "GET" request
####################################################################################################

# Sleep Safe landing page - accessed at localhost:5000 for now
@app.route("/", methods=['GET'])
def index():
    ''' displays the Sleep Safe landing page '''
    return render_template('index.html')

@app.route("/site", methods=['GET'])
def location_detail():
    ''' displays the location detail page about the site selected by the user '''
    return render_template('location.html')

# runs the app, always the last line
if __name__ == '__main__':
    app.run(threaded = True)