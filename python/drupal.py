import requests
from requests.auth import HTTPBasicAuth
from config import DRUPAL_API_URL, DRUPAL_API_PASS, HEADERS, DRUPAL_API_USER

def fetch_articles():
    response = requests.get(f'{DRUPAL_API_URL}/node/article', headers=HEADERS, auth=HTTPBasicAuth(DRUPAL_API_USER, DRUPAL_API_PASS))
    if response.status_code == 200:
        return response.json()
    return None

def create_article(json):
    response = requests.post(f'{DRUPAL_API_URL}/node/article', headers=HEADERS, auth=HTTPBasicAuth(DRUPAL_API_USER, DRUPAL_API_PASS), json=json)
    return response