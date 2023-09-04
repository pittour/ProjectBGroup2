from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from decouple import config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
app.config.from_object('config')

# Configuration pour la base de données de développement
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

# Configuration pour la base de données de test
app.config['SQLALCHEMY_DATABASE_URI_TEST'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

app.config['CACHE_TYPE'] = config("CACHE_TYPE")
app.config['CACHE_REDIS_URL'] = config("REDIS_URL")
app.config['CACHE_DEFAULT_TIMEOUT'] = config("DEFAULT_TIMEOUT")
cache = Cache(app)

CORS(app, resources={
     r"/*": {"origins": f"https://{config('DRUPAL_CONTAINER_NAME')}"}})

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

with app.app_context():
    db.create_all()
