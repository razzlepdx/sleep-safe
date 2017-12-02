from app import app, bcrypt, db
from flask import Flask, request, redirect, render_template, session, flash, url_for, make_response

from models import  User

from flask_login import login_user, login_required, logout_user, LoginManager, current_user

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
