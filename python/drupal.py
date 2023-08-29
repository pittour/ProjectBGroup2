import requests
import os
from requests.auth import HTTPBasicAuth
from config import DRUPAL_API_PASS, HEADERS, DRUPAL_API_USER

DRUPAL_API_URL=f"https://{os.environ['DRUPAL_CONTAINER_NAME']}/jsonapi"

def fetch_articles():
    response = requests.get(f'{DRUPAL_API_URL}/node/article', headers=HEADERS, auth=HTTPBasicAuth(DRUPAL_API_USER, DRUPAL_API_PASS), verify=False)
    if response.status_code == 200:
        return response.json()
    return None

def create_article(json):
    response = requests.post(f'{DRUPAL_API_URL}/node/article', headers=HEADERS, auth=HTTPBasicAuth(DRUPAL_API_USER, DRUPAL_API_PASS), json=json, verify=False)
    return response

def delete_article(id):
    response = requests.delete(f'{DRUPAL_API_URL}/node/article/{id}', headers=HEADERS, auth=HTTPBasicAuth(DRUPAL_API_USER, DRUPAL_API_PASS), verify=False)
    return response