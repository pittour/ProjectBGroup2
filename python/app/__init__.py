from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from decouple import config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
import os


os.environ['PROMETHEUS_MULTIPROC_DIR'] = '/tmp'
os.environ['prometheus_multiproc_dir'] = '/tmp'

app = Flask(__name__)
metrics = GunicornPrometheusMetrics(app)
app.config.from_object('config')

db = SQLAlchemy(app)

app.config['CACHE_TYPE'] = config("CACHE_TYPE")
app.config['CACHE_REDIS_URL'] = config("REDIS_URL")
app.config['CACHE_DEFAULT_TIMEOUT'] = config("DEFAULT_TIMEOUT")
cache = Cache(app)

CORS(app, resources={r"/*": {
    "origins": f"https://{config('DRUPAL_CONTAINER_NAME')}"}})

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

from app.view import bp
app.register_blueprint(bp)

# from app.models import Article
with app.app_context():
    db.create_all()
