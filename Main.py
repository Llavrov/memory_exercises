from flask import Flask, render_template, redirect, url_for, request

import json

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route('/')
@app.route('/Home')
def index():
    return render_template('Reg.html')


@app.route('/autho')
def enter():
    return render_template('autho.html')


@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/add')
def add_page():
    return render_template('add_page.html')


@app.route('/katalog')
def katalog_page():
    return render_template('katalog_page.html')


if __name__ == '__main__':
    app.run(debug=True)
