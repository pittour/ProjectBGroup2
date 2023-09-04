from app import app, db
import unittest
import json
from app.models import Article


class TestIntegrationAjouterArticle(unittest.TestCase):

    def setUp(self):
        # Utilise la base de données de test
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_ajouter_article(self):
        with app.app_context():
            db.create_all()

            articles_avant = Article.query.all()
            self.assertEqual(len(articles_avant), 0)

            article_data = {
                "title": "Mon Titre",
                "content": "Contenu de l'article"
            }

            response = self.app.post('/add_article', json=article_data)
            data = json.loads(response.get_data(as_text=True))

            self.assertEqual(response.status_code, 201)
            self.assertEqual(data, {'message': "Article added successfully"})

            articles_apres = Article.query.all()
            self.assertEqual(len(articles_apres), 1)
            nouvel_article = articles_apres[0]
            self.assertEqual(nouvel_article.article_title, "Mon Titre")
            self.assertEqual(nouvel_article.article_content,
                             "Contenu de l'article")


if __name__ == '__main__':
    unittest.main()
