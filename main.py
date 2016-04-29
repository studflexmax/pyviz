"""Top level module for your Flask application."""

import datetime
from pytz.gae import pytz

# Import the Flask Framework
from flask import Flask, render_template
app = Flask(__name__)

from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

# Don't need to call run() since the app is embedded within the App Engine WSGI
# application server.

# Configuration for FlatPages
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
FLATPAGES_MARKDOWN_EXTENSIONS = [
    'codehilite', 'headerid',
    'toc']
flatpages = FlatPages(app)
app.config.from_object(__name__)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

# For '/', render from markdown /content/misc/index.md.
@app.route('/')
def index(misc_dir='misc'):
    """Return a friendly HTTP greeting."""
    path = '{}/{}'.format(misc_dir, 'index')
    content = flatpages.get_or_404(path)
    return render_template("index.html", content=content)

# For '/', render from markdown /content/charts/<name>.md.
@app.route('/charts/<name>/')
def chart(name, charts_dir='charts'):
    path = '{}/{}'.format(charts_dir, name)
    content = flatpages.get_or_404(path)
    return render_template('index.html', content=content)

# For the pygments module.
@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
