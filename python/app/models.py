from app import db
from datetime import datetime
from config import DRUPAL_API_USER

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_drupal_id = db.Column(db.Integer, nullable=False)
    article_title = db.Column(db.String, nullable=False)
    article_content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.Column(db.String, default=DRUPAL_API_USER)