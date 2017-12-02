from flask import render_template
from app import app

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
