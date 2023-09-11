from flask import request, jsonify
from app import app, db, limiter, cache
from app.models import Article
from drupal import fetch_articles, create_article, delete_article
import bleach
from flask import Blueprint

bp = Blueprint("app", __name__)


@app.route('/get_articles', methods=['GET'])
@cache.cached()
@limiter.limit("30 per hour")
def get_articles():
    product_data = fetch_articles()
    if not product_data:
        return jsonify({"error": "Failed to fetch articles from drupal"}), 500
    
    
# Échappez les données de sortie à l'aide de bleach
    cleaned_data = bleach.clean(
        product_data, tags=[], attributes={}, styles=[], strip=True
    )
    
    return cleaned_data


@app.route('/add_article', methods=['POST'])
@limiter.limit("3 per hour")
def add_article():

    title = request.json.get('title')
    content = request.json.get('content')
    username = request.json.get('username') 
    password = request.json.get('password') 

    # limites de caractères maximales
    max_title_length = 100
    max_content_length = 1000

    # Tronquez le titre si nécessaire
    if len(title) > max_title_length:
        title = title[:max_title_length]

    # Tronquez le contenu si nécessaire
    if len(content) > max_content_length:
        content = content[:max_content_length]

    if not title or not content or not username or not password:
        return jsonify({
            "message": "Error : Title, Content, Username and/or Password not provided."
        }), 400

    # Échappez les données avant de les envoyer à Drupal
    title = bleach.clean(title, tags=[], attributes={}, strip=True)
    content = bleach.clean(content, tags=[], attributes={}, strip=True)

    data = {
        "data": {
            "type": "node--article",
            "attributes": {
                "title": title,
                "body": {
                    "value": content,
                    "format": "plain_text"
                }
            }
        }
    }
    response = create_article(username, password, json=data)

    if response.status_code == 201:
        article = Article(
            article_drupal_id=response.json()['data']['id'],
            article_title=title, article_content=content
        )
        db.session.add(article)
        db.session.commit()
        return jsonify({"message": "Article added successfully"}), 201

    return jsonify({"message": "Error : Article creation failed"}), 500


@app.route('/delete_article/<article_id>', methods=['DELETE'])
def supprimer_article(article_id):

    username = request.json.get('username') 
    password = request.json.get('password') 

    article = db.session.query(Article).filter_by(id=article_id).first()

    if article is None:
        return "Article non trouvé", 404

    id = article.article_drupal_id
    # Envoi de la requête DELETE à l'API Drupal pour supprimer l'article
    response = delete_article(id, username, password)

    # Si la suppression est réussie, renvoyer un message de succès
    if response.status_code == 204:
        article = Article.query.filter_by(id=article_id).first()
        db.session.delete(article)
        db.session.commit()
        return "Article supprimé avec succès !"
    else:
        return "Erreur lors de la suppression de l'article."


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500
