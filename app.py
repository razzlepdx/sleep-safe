from flask import Flask, request, redirect, render_template, flash, url_for, json, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
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

bcrypt = Bcrypt(app)
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
    green_tent = url_for('static', filename='images/Pin-Tent-Green.png')
    red_tent = url_for('static', filename='images/Pin-Tent-Red.png')
    user_location = url_for('static', filename='images/Dot-User-Location.png')
    mymap = Map(
        identifier="mymap",
        lat=45.5183037,
        lng=-122.6810941,
        markers=[
          {
             'icon': green_tent,
             'lat': 45.5333114,
             'lng': -122.7058782,
             'infobox': "<div style='float:left;'>" +
             			"<p style='margin-top:0; font-weight: bold;'>Wallace Park</p>" +
             			"<p style='margin-top:0;'><span style='color: green; font-weight: bold;'>Safe Rating: 80%</span></p>" +
             			"</div>" +
             			"<div style='float:right; font-size:40px; font-weight: bold; margin-left: 10px;'>" +
             			"<a href='./site' style='text-decoration:none; color:#a4d4ff;'>></a>" +
             			"</div>" +
             			"</div>"
          },
          {
             'icon': green_tent,
             'lat': 45.5126438,
             'lng': -122.7149248,
             'infobox': "<div style='float:left;'>" +
             			"<p style='margin-top:0; font-weight: bold;'>Oaks Park</p>" +
             			"<p style='margin-top:0;'><span style='color: green; font-weight: bold;'>Safe Rating: %67</span></p>" +
             			"</div>" +
             			"<div style='float:right; font-size:40px; font-weight: bold; margin-left: 10px;'>" +
             			">" +
             			"</div>" +
             			"</div>"
          },
          {
             'icon': red_tent,
             'lat': 45.4724105,
             'lng': -122.6648244,
             'infobox': "<div style='float:left;'>" +
             			"<p style='margin-top:0; font-weight: bold;'>Puppet</p>" +
             			"<p style='margin-top:0;'><span style='color: red; font-weight: bold;'>Safe Rating: 20%</span></p>" +
             			"</div>" +
             			"<div style='float:right; font-size:40px; font-weight: bold; margin-left: 10px;'>" +
             			">" +
             			"</div>" +
             			"</div>"
          },
          {
             'icon': user_location,
             'lat': 45.5183037,
             'lng': -122.6810941
          }          
        ],
        style="height:73vh;width:100%;margin:0;",
        zoom=11,
        maptype_control=False,
        streetview_control=False,
        fullscreen_control=False
    )  
    return render_template('index.html', mymap=mymap, green_tent=green_tent, red_tent=red_tent)

@app.route("/site", methods=['GET'])
def location_detail():
    ''' displays the location detail page about the site selected by the user '''
    return render_template('location.html')

# runs the app, always the last line
if __name__ == '__main__':
    app.run(threaded = True)