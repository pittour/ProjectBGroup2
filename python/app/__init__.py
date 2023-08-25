from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
cache = Cache(app)

from app import models
with app.app_context():
    db.create_all()
from . import view

