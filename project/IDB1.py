#!/usr/bin/env python
"""Implementation of flask app for serving HTML pages"""

import os
from flask import Flask, render_template, send_from_directory
from models import *

APP = Flask(__name__)
@APP.route('/')
def render_home():
    """Return index.html page when no path is given"""
    return render_template('index.html')

@APP.route('/about/')
def render_about():
    """Return HTML page stored in templates directory"""
    return render_template('about.html')

@APP.route('/index/')
def render_index():
    """Return HTML page stored in templates directory"""
    return render_template('index.html')

# We assume this will always list out database entries
@APP.route('/detail/')
def render_detail():
    """Return HTML page stored in templates directory"""
    myUni_all = University.query.all()
    return render_template('detail.html', myUni_all = myUni_all)


@APP.route('/university/')
def render_uni_table():
    """Return HTML page stored in templates directory"""
    entries = University.query.all()
    return render_template('table.html', entries=entries, title="Universities")

@APP.route('/city/')
def render_city_table():
    """Return HTML page stored in templates directory"""
    entries = City.query.all()
    return render_template('table.html', entries=entries, title="Cities")

@APP.route('/major/')
def render_uni_table():
    """Return HTML page stored in templates directory"""
    entries = Major.query.all()
    return render_template('table.html', entries=entries, title="Majors")

# @APP.route('/Ethnicity/')
# def render_uni_table():
#     """Return HTML page stored in templates directory"""
#     entires = Ethnicity.query.all()
#     return render_template('table.html', entries=entries, title="Ethnicities")

# @APP.route('/<string:page_name>/')
# def render_static(page_name):
#     """Return HTML page stored in templates directory"""
# return render_template('%s' % page_name)


@APP.route('/favicon.ico')
def favicon():
    """Return the favicon.ico"""
    return send_from_directory(os.path.join(APP.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    APP.run()
