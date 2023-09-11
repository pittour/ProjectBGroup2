##Collaborateurs:
* [Hadi Hassan](https://github.com/hassanhadi1)
* [Kevin Billerache](https://github.com/pittour)
* [Christoph Dufetre](https://github.com/Sparkly74)

# Transformation de l'Application Monolithique en Micro-services
Ce projet a pour objectif de transformer une application monolithique Drupal en une architecture de micro-services,
permettant d'ajouter/supprimer des articles. Le projet utilise Python et Flask pour créer les services web, Docker pour la conteneurisation,
Jenkins pour l'automatisation du pipeline CI/CD, et Drupal pour l'interface utilisateur
 ---------------------------------------------------------------------------------------------------------------------------------
## Prérequis

- Accès au code source de l'application Drupal.
- Environnement de développement local configuré.
- Git installé sur votre système.
- Compte sur une plateforme CI/CD (par exemple, GitLab CI/CD, Travis CI, Jenkins).
- Connaissance de base des concepts de micro-services. 
---------------------------------------------------------------------------------------------------------------------------------
## Structure du Projet
Le projet est organisé en plusieurs dossiers, chacun jouant un rôle essentiel dans la transformation de l'application monolithique en micro-services.

### Dossier Drupal

Le dossier "drupal" contient les fichiers nécessaires pour le déploiement de l'application Drupal en https.

#### Dockerfile

Le Dockerfile permet de construire l'image Docker de l'application Drupal. Voici les principales étapes effectuées dans ce fichier :

- Utilisation d'une image de base officielle de Drupal avec Apache.
- Installation des dépendances.
- Configuration de l'environnement, y compris l'ajout du chemin Composer.
- Copie des scripts d'entrée personnalisés, du fichier php.ini, et des configurations SSL.
- Gestion des autorisations et répertoires.
- Installation de Composer, Drush, et d'autres dépendances.
- Génération des clés SSL et configuration d'Apache.

#### Docker-compose.yml

Le fichier docker-compose.yml définit les services Docker nécessaires pour exécuter l'application Drupal et sa base de données MySQL. Il configure également les variables d'environnement à partir du fichier .env.

#### .env

Le fichier .env contient les variables d'environnement nécessaires pour configurer la base de données MySQL et d'autres paramètres liés à Drupal.
Il faut utiliser le fichier .env.exemple pour definir les variables necessaires. 

### entrypoint.sh 

installe l'application drupal, et configure les modules necessaires 


### Dossier python 
ce dossier contient le micro service flask, qui effectue des operations CRUD sur les article du blog drupal

#### init.py 
c'est le point d'entrée de l'application.
nous utilison une bas de donnée SQLITE gerée par SQLALCHEMY afin d'enregistrer les operation effectuer via le micro service.
Flask_cors nous permet de definir les serveurs pouvant se connecter à notre micro_service.
Flask_caching avec Redis nous permet de mettre en cache les resultat d'une requete.
Flask_limiteur limite le nombre de requete effectuer par un utilisateur sur une period de temps donnée.

#### view.py 
Il defini les endpoints de notre API Flask :
/get_articles : permet de recuperer la liste des articles depuis drupal.
/add_article : permet d'ajouter un nouvel article à drupal.
/delet_article/<ID> : permet de suprimer un article.

#### .env
Le fichier .env contient les variables d'environnement nécessaires pour configurer le micro_service.
Il faut utiliser le fichier .env.exemple pour definir les variables necessaires. 

#### tests
ces fichiers contiennent les tests unitaire de notre application.

#### config-gunicorn.py
ce fichier expose les metriques de suivie de notre application sur le port 9200 afin de les relier à Prometheus.











******************************************************************************************************
******************************************************************************************************
******************************************************************************************************
******************************************************************************************************
******************************************************************************************************
******************************************************************************************************

---------------------------------------------------------------------------------------------------------------------------------

[From Monolith to Microservices: A Guide To Replatforming](https://fabric.inc/blog/commerce/from-monolith-to-microservices)


---------------------------------------------------------------------------------------------------------------------------------

## II ) CHOIX DE L'APPLICATION CMS A MIGRER : DRUPAL

![My Image](drupal-architecture.jpg)

### PRESENTATION ET ANALYSE DE L'ARCHITECTURE:

Users − These are the users on the Drupal community. The user sends a request to a server using Drupal CMS and web browsers, search engines, etc. acts like clients.

Administrator − Administrator can provide access permission to authorized users and will be able to block unauthorized access. Administrative account will be having all privileges for managing content and administering the site.

Drupal − Drupal is a free and open source Content Management System (CMS) that allows organizing, managing and publishing your content and is built on PHP based environments. Drupal CMS is very flexible and powerful and can be used for building large, complex sites. It is very easy to interact with other sites and technologies using Drupal CMS. Further, you will be able to handle complex forms and workflows.

PHP − Drupal uses PHP in order to work with an application which is created by a user. It takes the help of web server to fetch data from the database. PHP memory requirements depend on the modules which are used in your site. Drupal 6 requires at least 16MB, Drupal 7 requires 32MB and Drupal 8 requires 64MB.

Web Server − Web server is a server where the user interacts and processes requests via HTTP (Hyper Text Transfer Protocol) and serves files that form web pages to web users. The communication between the user and the server takes place using HTTP. You can use different types of web servers such as Apache, IIS, Nginx, Lighttpd, etc.

Database − Database stores the user information, content and other required data of the site. It is used to store the administrative information to manage the Drupal site. Drupal uses the database to extract the data and enables to store, modify and update the database.

---------------------------------------------------------------------------------------------------------------------------------
# JOUR 2

## AUTOMATISATION  DE L'INSTALLATION DE DRUPAL ( JOUR 2 + 3)

CONTENEURISATION AVEC DOCKER COMPOSE :
 - UN CONTENEUR MYSQL
 - UN CONTENEUR DRUPAL

Image docker: docker pull drupal:7.98-php8.2-fpm-bullseye

Fichier Docker Compose : Docker compose drupal + msql.png

##  IDENTIFICATION DES DIFFERENTES FONCTIONNALITES MIGRABLES :

### 1- Gestion d'utilisateurs et d'authentification :
      Créer un micro-service pour gérer l'authentification, l'inscription des utilisateurs et la gestion des profils. Cela 
      pourrait permettre aux utilisateurs de s'authentifier de manière centralisée, même si d'autres parties de l'application 
      sont déployées en micro-services distincts.
### 2- Notifications : 
       Créer un micro-service pour gérer l'envoi de notifications par e-mail, SMS ou d'autres canaux.
### 3- Analyse et suivi :
       Créer un micro-service pour collecter et analyser les données de suivi et les statistiques d'utilisation.
       

## MISE EN PLACE D'UN MICRO SERVICE : AJOUTER UN ARTICLE SUR LE SITE EN DEMO

### Extension Services Web: Installation du module JSON:API  pour exposer les entités en tant qu'API web JSON:API-specification-compliant

http://localhost:8080/jsonapi

http://localhost:8080/jsonapi/node/article

### Extension Services Web: Installation du module HTTP Basic Authentification:
Installé
	Nom
	Description
	HTTP Basic Authentication 	
Provides an HTTP Basic authentication provider.
Nom système : basic_auth
Version : 10.1.2
 

### Authentication API overview (https://www.drupal.org/docs/8/api/authentication-api/overview)

Setup Access Token / OAuth Based Authentication (https://www.drupal.org/docs/contributed-modules/api-authentication/setup-access-token-oauth-based-authentication)

Installation du module : RESTful Web Services (Drupal REST & JSON API Authentication)

Drupal REST & JSON API Authentication module restricts and secures unauthorized access to your Drupal site APIs using different authentication methods including Basic Authentication , API Key Authentication , JWT Authentication , OAuth Authentication , External / Third-Party Provider Authentication, etc:

 CHOIX DE L'AUTHENTIFICATION => BASIC AUTHENTIFICATION

A REST API defines a set of functions in which developers can perform requests such as GET, POST, PUT, PATCH, DELETE, and receive responses via HTTP protocol. For example, when a client application calls a Drupal API to fetch a specific user (the resource), the API will return the state of that user, including their name, email, user id, etc.


Routing system overview (https://www.drupal.org/docs/drupal-apis/routing-system/routing-system-overview)

---------------------------------------------------------------------------------------------------------------------------------
JOUR 3:

### FIN DE L'AUTOMATISATION  DE L'INSTALLATION DE DRUPAL ( JOUR 2 + 3)


### CREATION DU CODE PYTHON SOUS FLASK DU MICRO-SERVICE permettant d'ajouter un article au site.


### UTILISATION DE THUNDERBIRD SOUS VSCODE POUR TESTER L'API DU MICROSERVICE (GET, POST)


---------------------------------------------------------------------------------------------------------------------------------
JOUR 4:

### FEUILLE DE ROUTE POUR LE DEVELOPPEMENT DU MICRO SERVICE :

1. Configuration de l'environnement :
Installation de Flask, SQLAlchemy et autres dépendances nécessaires.
Configuration de la base de données pour le micro-service.
2. Connexion au monolithe Drupal :
Utilisation de la bibliothèque requests pour intégrer l'API REST de DRUPAL.
3. Définition du modèle de données :
Modélisation de la commande dans SQLAlchemy.
4. Implémentation des routes :
Création de routes pour l'ajout au panier, la vérification des disponibilités, et
d'autres actions nécessaires.
5. Gestion des erreurs :
Ajout de gestionnaires d'erreurs pour traiter les réponses non 200, les
timeouts, etc.
6. Optimisation et sécurité :
Mise en cache des réponses fréquemment utilisées.
Gestion des taux d'appels à l'API pour respecter les limites imposées.


## DEBUT PHASE DE CREATION DES TESTS MICRO_SERVICE.PY AVEC UNITEST
## Test d'Intégration : Ajout d'un Article

Ce test d'intégration vise à vérifier la fonctionnalité d'ajout d'un article dans le micro-service. Il assure que l'API réagit correctement aux demandes POST pour créer de nouveaux articles en vérifiant la création réussie de l'article et en inspectant ses détails.

**Description du Test :**

1. **Configuration de la Base de Données :** Le test configure une base de données SQLite pour s'assurer que l'environnement de test est propre et isolé.

2. **Ajout d'un Article :** Le test envoie une requête POST à l'endpoint `/add_article` avec des données JSON simulées pour un nouvel article, comprenant un titre et un contenu.

3. **Validation de la Réponse :** Il vérifie que la réponse HTTP est conforme à la norme (statut 201 - Créé avec succès) et que le message de réponse indique "Article added successfully".

4. **Vérification en Base de Données :** Le test interroge la base de données pour s'assurer qu'un nouvel article a été créé avec les détails attendus, notamment le titre et le contenu.

**Raison du Test :**

Ce test garantit que le micro-service est capable de gérer avec succès les demandes d'ajout d'articles, qu'il stocke correctement les données dans la base de données, et qu'il renvoie une réponse appropriée pour informer le client de la réussite de l'opération.

## Test d'Intégration : Suppression d'un Article

Ce test d'intégration vise à vérifier la fonctionnalité de suppression d'un article dans le micro-service. Il s'assure que l'API est capable de gérer les demandes DELETE pour supprimer des articles existants de manière fiable.

**Description du Test :**

1. **Configuration de la Base de Données :** Le test configure une base de données SQLite pour garantir un environnement de test propre et isolé.

2. **Ajout d'un Article à Supprimer :** Le test ajoute d'abord un article factice à la base de données en envoyant une requête POST à l'endpoint `/add_article`.

3. **Suppression de l'Article :** Ensuite, le test envoie une requête DELETE à l'endpoint `/node/article/<article_id>` pour supprimer l'article précédemment ajouté.

4. **Validation de la Réponse :** Il vérifie que la réponse HTTP renvoyée est conforme à la norme (statut 200 - OK).

5. **Vérification en Base de Données :** Le test interroge la base de données pour s'assurer que l'article a bien été supprimé.

**Raison du Test :**

Ce test garantit que le micro-service peut gérer correctement les demandes de suppression d'articles, en veillant à ce que les données soient supprimées de la base de données et que le système renvoie une réponse appropriée. Cela garantit également que le système gère correctement les opérations de suppression, ce qui est essentiel pour maintenir des données cohérentes et éviter les erreurs.


## DEFINITION DU MODELE DE DONNEES : Modélisation dans SQLAlchemy.

SQLAlchemy est un outil fondé sur le principe de mapping objet-relationnel (ORM).

SQLAlchemy facilite donc la liaison entre Python et les bases de données SQL en convertissant automatiquement les appels de classes de Python en instructions SQL. Il est donc possible de requêter les bases de données relationnelles de manière pythonique.

Notre code python sera le même pour tous les environnements et dialectes SQL tels que SQlite, PostGReSQL ou Oracle. Cela améliore l’interopérabilité avec le reste de notre application et on peut ainsi changer de système de base de données sans avoir à changer son code.

L’écriture des contraintes sur le schéma des tables directement depuis notre script python.

Au lieu de jongler entre les différents dialectes SQL, le toolkit open source SQL Alchemy nous permet ainsi de rationaliser notre workflow et de traiter efficacement nos données depuis le langage Python.


Pros and Cons of SQL Alchemy

Pros

    Alchemy gives abstraction to the backend database. So, an average developer does not have to worry about SQL statements.
    The transition to other databases becomes easier.
    Queries are optimized and may work better than SQL if you wrote it yourself unless you are an SQL veteran.

Cons

    There could be instances where Alchemy might become inefficient. Therefore, knowing SQL is always desired.
    Knowing what is happening under the hood often gives an edge. So, it is not a complete replacement for SQL.


## 5. GESTION DES ERREURS (EN COURS)
Ajout de gestionnaires d'erreurs pour traiter les réponses non 200, etc...



---------------------------------------------------------------------------------------------------------------------------------
## JOUR 5:

## OPTIMISATION DU MICRO-SERVICE

### 1) Mise en cache des réponses fréquemment utilisées avec REDIS

### 2 ) Gestion des taux d'appels à l'API pour respecter les limites imposées avec Flask-Limiter

## SECURISATION DU MICRO-SERVICE

### 1 ) Installation de Python-Decouple
Pour sécuriser la clé API de DRUPAL  : Plutôt que de la stocker dans config.py ,
utilisez des variables d'environnement. Vous pouvez utiliser python-decouple pour
aider à gérer cela.

### Création Docker File sur une base de déploiement Gunicorn pour notre Micro-Service

### ETUDE MISE EN PLACE D'UN CONTENEUR NGINX (pour sécuriser les échanges entre les utilisateurs et notre DRUPAL):

Création en cours du fichier nginx.conf qui sera injecté dans le docker conteneur NGINX


----------------------------------------------------------------------------------------------------------------------------------------
 ## JOUR 6:

### INSTALLATION DU CERTIFICAT SSL SUR LE CONTENEUR DRUPAL
  
 ### MISE EN PLACE DE LA BASE DE DONNEES AVEC SQL ALCHEMY

 ### TRACKING DE L'ID DES REQUETES DANS DRUPAL

 ----------------------------------------------------------------------------------------------------------------------------------------
## JOUR 7  : OBJECTIFS

### FINIR LA ROUTE DE LA SECONDE PARTIE DU MICRO-SERVICE PERMETTANT DE DELETE UN ARTICLE (validé)

### DOCKERISER LE MICROSERVICE (validé)

### INSTALLER LE SERVICE NGINX SUR LE CONTENEUR DU MICRO SERVICE (EN COURS): installation de procps pour superviser les services (gunicorn, nginx,...) ==> pas de systemctl (validé)

### CREATION D'UN FRONT END POUR NOTRE MICRO-SERVICE : GRAPHICAL USER INTERFACE (HADI) => Ajout d'article / Suppression d'article (EN COURS)

----------------------------------------------------------------------------------------------------------------------------------------
## JOUR 8 :

### CONFIGURER LE CERTIFICAT SUR LE CONTENEUR DU MICRO SERVICE

### PROJECTION AUTOMATISATION VIA JENKINS CI/CD

OPTION 1 : utilisation de la méthode DinD (Docker in Docker) : création d'un conteneur jenkins qui lui même doit créer les conteneurs drupal, mysql, microservice.
(https://www.jenkins.io/doc/book/installing/docker/)

Problèmes rencontrés: difficulté réseau et reconnaissance des ports entre les différents conteneurs.
Abandon de cette option

----------------------------------------------------------------------------------------------------------------------------------------
## JOUR 9 :
 
### PROJECTION AUTOMATISATION VIA JENKINS CI/CD (SUITE)

NOUVELLE METHODE:
Activer l’utilisation du démon Docker dans le conteneur Jenkins

Connexion de l'interface de ligne de commande Docker dans le conteneur Jenkins au démon Docker sur la machine hôte en fixant la prise du démon dans le conteneur avec l’indicateur -v. On ajoute l’argument suivant : /var/run/docker.sock:/var/run/docker.sock lorsqu'on exécute l’image :

docker run -it -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home custom-jenkins-docker


Fichier dockerfile de notre JENKINS CUSTOM:

FROM jenkins/jenkins:lts
USER root
RUN apt-get update -qq \
    && apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/debian \
$(lsb_release -cs) \
stable"
RUN apt-get update  -qq \
    && apt-get -y install docker-ce
RUN usermod -aG docker jenkins
RUN apt-get install -y python3 python3-pip python3-venv


 
 
 
 EN ATTENTE : TEST ADDITIONNEL Utiliser pyflakes 3.1.0 (pip install pyflakes)

 ----------------------------------------------------------------------------------------------------------------------------------------


 



 




