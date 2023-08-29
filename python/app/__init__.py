from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from decouple import config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

app.config['CACHE_TYPE'] = config("CACHE_TYPE")
app.config['CACHE_REDIS_URL'] = config("REDIS_URL")
app.config['CACHE_DEFAULT_TIMEOUT'] = config("DEFAULT_TIMEOUT")
cache = Cache(app)

CORS(app, resources={r"/*": {"origins": f"https://{os.environ['DRUPAL_CONTAINER_NAME']}"}})

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

from app import models
with app.app_context():
    db.create_all()
from . import view

