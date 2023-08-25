from flask import request, jsonify
from app import app, db, limiter, cache
from app.models import Article
from drupal import fetch_articles, create_article

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
        article = Article(article_title=title, article_content=content)
        db.session.add(article)
        db.session.commit()
        return jsonify({"message": "Article added successfully"}), 201
    
    return jsonify({"message": "Error : Article creation failed"}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500