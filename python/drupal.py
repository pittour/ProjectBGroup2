import requests
from requests.auth import HTTPBasicAuth
from config import HEADERS
from decouple import config

DRUPAL_API_URL = f"https://{config('DRUPAL_CONTAINER_NAME')}/jsonapi"


def fetch_articles():
    response = requests.get(f'{DRUPAL_API_URL}/node/article', headers=HEADERS,
                            verify=False)
    if response.status_code == 200:
        return response.json()
    return None


def create_article(username, password, json):
    response = requests.post(f'{DRUPAL_API_URL}/node/article', headers=HEADERS,
                             auth=HTTPBasicAuth
                             (username, password), json=json,
                             verify=False)
    return response


def delete_article(id, username, password):
    username = config('DRUPAL_API_USER')
    password = config('DRUPAL_API_PASS')
    response = requests.delete(f'{DRUPAL_API_URL}/node/article/{id}',
                               headers=HEADERS,
                               auth=HTTPBasicAuth
                               (username, password),
                               verify=False)
    return response
