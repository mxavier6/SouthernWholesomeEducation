"""Implementation of flask app for serving HTML pages"""

import os
from flask import Flask, render_template, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
APP = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from models import DB, University
@APP.route('/')
def render_home():
    """Return index.html page when no path is given"""
    return render_template('index.html')

@APP.route('/about/')
def render_about():
    """Return HTML page stored in templates directory"""
    return render_template('about.html')

# We assume this will always list out database entries
@APP.route('/detail/')
def render_detail():
    """Return HTML page stored in templates directory"""
    return render_template('detail.html', myVar = [42, 54, 34])


# @APP.route('/university/<string:uni_name>/')
# def render_uni_detail():
#     """Return index.html page when no path is given"""
#     myUni = University.query.all()
#     return render_template('detail.html', myUni=myUni)


@APP.route('/favicon.ico')
def favicon():
    """Return the favicon.ico"""
    return send_from_directory(os.path.join(APP.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    APP.run()
