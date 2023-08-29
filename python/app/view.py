from flask import request, jsonify
from app import app, db, limiter, cache
from app.models import Article
from drupal import fetch_articles, create_article, delete_article

@app.route('/get_articles', methods=['GET'])
@cache.cached()
@limiter.limit("5 per hour")
def get_articles():
    product_data = fetch_articles()
    if not product_data:
        return jsonify({"error": "Failed to fetch articles from drupal"}), 500
    
    return product_data

@app.route('/add_article', methods=['POST'])
@limiter.limit("3 per hour")
def add_article():
    title = request.json.get('title')
    content = request.json.get('content')

    if not title or not content:
        return jsonify({"message": "Error : Title and/or Content not provided."}), 400
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
    response = create_article(json=data)

    if response.status_code == 201:
        article = Article(article_drupal_id=response.json()['data']['id'], article_title=title, article_content=content)
        db.session.add(article)
        db.session.commit()
        return jsonify({"message": "Article added successfully"}), 201
    
    return jsonify({"message": "Error : Article creation failed"}), 500

@app.route('/node/article/<article_id>', methods=['DELETE'])
def supprimer_article(article_id):
    
    id = Article.query.get(article_id).article_drupal_id
    # Envoi de la requête DELETE à l'API Drupal pour supprimer l'article
    response = delete_article(id)

    # Si la suppression est réussie (statut 204), renvoyer un message de succès
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