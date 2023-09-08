from app import app, db
import unittest
from app.models import Article


class TestIntegrationSupprimerArticle(unittest.TestCase):

    def setUp(self):
        # Utilise la base de données de test.
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        with app.app_context():
            db.session.query(Article).delete()
            db.session.commit()
            db.session.remove()
            

    def test_supprimer_article(self):
        with app.app_context():

            # Ajoutez un article à la base de données pour le supprimer ensuite
            article_data = {
                "title": "Article à supprimer",
                "content": "Contenu de l'article à supprimer"
            }
            response = self.app.post('/add_article', json=article_data)
            self.assertEqual(response.status_code, 201)

            articles_avant_suppression = Article.query.all()
            self.assertEqual(len(articles_avant_suppression), 1)

            article_a_supprimer = articles_avant_suppression[0]
            article_id = article_a_supprimer.id

            # Supprimez l'article
            response = self.app.delete(f'/node/article/{article_id}')
            self.assertEqual(response.status_code, 200)

            articles_apres_suppression = Article.query.all()
            self.assertEqual(len(articles_apres_suppression), 0)


if __name__ == '__main__':
    unittest.main()