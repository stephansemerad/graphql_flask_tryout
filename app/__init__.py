'''
Thanks to https://www.jorgehernandezramirez.com/2020/03/21/flask-and-graphql-filters-graphene-sqlalchemy-filters/
'''
from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_FOLDER']        = 'templates'

db              = SQLAlchemy(app)

from app.views import *
from app.initialize import *

initialize()