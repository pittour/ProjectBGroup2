from app import app
import unittest
import json


class TestAjouterArticle(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ajouter_article(self):
        article_data = {
            "title": "Mon Titre",
            "content": "Contenu de l'article"
        }

        response = self.app.post('/add_article', json=article_data)
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, {'message': "Article added successfully"})

if __name__ == '__main__':
    unittest.main()