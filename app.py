from flask import Flask, request, redirect, render_template, flash, url_for, json, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import os
from keys import *

# app and db dev environment settings:
######################################
db_uri = 'mysql+pymysql://sleep-safe:sleep-safe@localhost:8889/sleep-safe'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ZAj08N/$3m]XHjHy!rX R/~?X,9RW@UL'

db = SQLAlchemy(app)
GoogleMaps(app, key=keys())

# routes:
# all routes get a decorator `@app.route` that takes at least one parameter - the url.  
# optional parameter: HTTP request types go here too.  if left blank it defaults to a "GET" request
####################################################################################################

# Sleep Safe landing page - accessed at localhost:5000 for now
@app.route("/", methods=['GET'])
def index():
    ''' displays the Sleep Safe map '''
    mymap = Map(
        identifier="mymap",
        lat=45.5435634,
        lng=-122.674997,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 45.5435634,
             'lng': -122.674997,
             'infobox': "<b>Puppet</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 45.4724105,
             'lng': -122.6648244,
             'infobox': "<b>Oaks Park</b>"
          }
        ],
        zoom=10,
        maptype_control=False,
        streetview_control=False,
        fullscreen_control=False
    )  
    return render_template('index.html', mymap=mymap)

@app.route("/site", methods=['GET'])
def location_detail():
    ''' displays the location detail page about the site selected by the user '''
    return render_template('location.html')

# runs the app, always the last line
if __name__ == '__main__':
    app.run(threaded = True)