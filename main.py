"""`main` is the top level module for your Flask application."""

import datetime
from pytz.gae import pytz

# Import the Flask Framework
from flask import Flask, render_template
app = Flask(__name__)

from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
FLATPAGES_MARKDOWN_EXTENSIONS = [
    'codehilite', 'headerid',
    'toc']
CHARTS_DIR = 'charts'
MISC_DIR = 'misc'

flatpages = FlatPages(app)
freezer = Freezer(app)

app.config.from_object(__name__)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    path = '{}/{}'.format(MISC_DIR, 'index')
    content = flatpages.get_or_404(path)
    return render_template("index.html", content=content)

@app.route('/charts/<name>/')
def chart(name):
    path = '{}/{}'.format(CHARTS_DIR, name)
    content = flatpages.get_or_404(path)
    return render_template('index.html', content=content)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
