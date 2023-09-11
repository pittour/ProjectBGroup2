##Collaborateurs:
* [Hadi Hassan](https://github.com/hassanhadi1)
* [Kevin Billerache](https://github.com/pittour)
* [Christophe Dufetre](https://github.com/Sparkly74)

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

## Architecture du PROJET

![My Image](/images/Diagramme.png)

### Drupal

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


### Micro Service (Python)  
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

#### requirements.txt
Contient la liste des dependances necessaire à l'application flask.

#### Dockerfile

Le Dockerfile permet de construire l'image Docker du micro_service. Voici les principales étapes effectuées dans ce fichier :

- Utilisation d'une image de base officielle de python3 avec Debian.
- Installation des dépendances.
- Copie des fichiers du micro_service.
- Gestion des autorisations pour l'utilisateur Nginx.
- Génération des clés SSL et configuration de Nginx.
- Mis en place des fichiers WAF.
- Configuration de pare feu UFW



### UFW (Uncomplicated Firewall)

Outil de gestion de pare-feu pour les systèmes Linux, y compris Debian. Il simplifie la configuration et la gestion des règles de pare-feu, ce qui le rend adapté à une utilisation sur des serveurs Debian. 
 

AVANTAGES: 

   - Sécurité : UFW nous permet de définir des règles de pare-feu pour limiter les connexions réseau entrantes et sortantes, ce qui renforce la sécurité de notre système. 

   - Simplicité : Comme son nom l'indique, UFW est conçu pour être simple à utiliser. Il fournit une interface conviviale pour gérer les règles de pare-feu, ce qui le rend adapté aux utilisateurs novices. 

   - Gestion centralisée : UFW peut simplifier la gestion de os règles de pare-feu en les regroupant en ensembles de règles (profiles) pour différents services ou applications. 

   - Intégration Debian : UFW s'intègre bien avec d'autres applications et services, ce qui en fait un choix populaire pour la gestion des pare-feu. 

   - Documentation abondante : En raison de sa popularité, UFW dispose d'une documentation étendue et d'une communauté active. Vous pouvez trouver de l'aide facilement en cas de besoin. 

  

INCONVENIENTS:  

   - Limitation de complexité : Si vous avez besoin de règles de pare-feu très complexes et spécifiques, UFW peut s'avérer limité. Dans ce cas, vous pourriez préférer utiliser iptables directement. 

    - Absence de fonctionnalités avancées : UFW est conçu pour simplifier la gestion des règles de pare-feu, mais il peut manquer certaines fonctionnalités avancées que vous trouveriez dans des pare-feu plus complets comme iptables. 

    - Pas d'interface graphique : Bien qu'UFW propose une interface en ligne de commande simple, il n'a pas d'interface graphique officielle. Si vous préférez une interface graphique, vous devrez peut-être utiliser un outil tiers pour le gérer visuellement. 

    Performance : Bien qu'UFW n'ait généralement pas un impact significatif sur les performances, l'ajout de règles de pare-feu complexes peut potentiellement entraîner une surcharge, surtout sur des systèmes à haute charge. 

    - Possibilité de blocage accidentel : En raison de sa simplicité, il est possible de configurer UFW de manière incorrecte et de bloquer accidentellement des connexions réseau.

      
 
![My Image](/images/UFWsetup.png)



 Tout ce qui n'est pas déclaré est bloqué par défaut :

- Installation du package ufw 
- Autorisation des port 443, 80 et 8000 pour le protocole TCP 
- Blocage de toutes les requêtes entrantes sur les autres ports (profil default) 
- Autorisation des requêtes en sortie (pour les ports autorisés) 
- Possibilité de suivre les logs et de paramétrer en medium les logs (par défaut en low et stocké dans /var/log/ufw.log)


 Objectif : Protéger notre serveur contre les attaques réseau telles que :

- Attaques DDoS (Distributed Denial of Service) : En n'autorisant que le trafic TCP sur ces ports, vous pouvez limiter la bande passante disponible pour les attaques DDoS qui tentent de submerger votre serveur avec un trafic illégitime. Cela peut aider à atténuer l'impact de ces attaques en les filtrant.

- Attaques de reconnaissance : Les pirates informatiques effectuent souvent des scans de ports pour identifier les services en cours d'exécution sur un serveur. En n'autorisant que le TCP sur les ports 80 et 443, vous réduisez la surface d'attaque en limitant les services accessibles depuis l'extérieur.

- Attaques par force brute : Les attaques par force brute tentent de deviner des mots de passe en essayant différentes combinaisons. En autorisant uniquement le trafic TCP sur les ports HTTP (80) et HTTPS (443), vous pouvez réduire la surface d'attaque, car seuls les services Web sont accessibles depuis l'extérieur.

- Attaques d'injection SQL : En limitant l'accès aux ports HTTP et HTTPS, vous réduisez la possibilité pour les attaquants d'exploiter des vulnérabilités de sécurité telles que les injections SQL via des formulaires Web. Cependant, cela ne protège pas complètement contre de telles attaques, car elles peuvent encore être lancées via le trafic HTTP autorisé.

- Attaques de vol de données : En restreignant l'accès aux ports HTTP et HTTPS, vous réduisez le risque d'accès non autorisé aux données sensibles stockées sur votre serveur Web. Cela peut contribuer à la protection de données sensibles, comme les informations de paiement sur un site de commerce électronique.


 


### SERVICE NGINX

L’objectif est de paramétrer le service Nginx au plus près des besoins de notre micro-service pour garantir la confidentialité, l'intégrité et la disponibilité des données et des fonctionnalités que le microservice expose et pour le protéger contre : des injections SQL, des injections de script, des attaques à force brute, ... 


FONCTIONNALITES : 


Serveur web statique : Nginx peut être utilisé pour servir des fichiers HTML, CSS, JavaScript et d'autres fichiers statiques, ce qui en fait une excellente option pour l'hébergement de sites web. 

Reverse Proxy : Nginx peut agir en tant que proxy inverse pour rediriger le trafic vers différents serveurs en fonction de règles de routage, ce qui permet de gérer la répartition de la charge et d'améliorer la disponibilité du service. 

Terminaison SSL/TLS : Nginx peut gérer la terminaison SSL/TLS pour sécuriser les connexions entre les clients et les serveurs. 

Cache HTTP : Nginx peut mettre en cache des réponses HTTP pour réduire la charge du serveur et améliorer les performances. 

Protection contre les attaques DDoS : Nginx peut être utilisé pour atténuer les attaques DDoS en filtrant le trafic malveillant. 

Réécriture d'URL : Nginx permet de réécrire les URL pour les rendre plus conviviales ou pour gérer les redirections. 

Gestion des connexions : Nginx peut gérer efficacement un grand nombre de connexions simultanées, ce qui en fait un choix populaire pour les sites web à fort trafic. 



#### CONFIGURATION DU FICHIER Nginx.conf


Paramétrage  de notre reverse proxy en lien avec Gunicorn et la securisation de notre serveur via des en-tete permettant la mise en place de politique de securité. Il limite egalement le nombre de requetes pour evité une surcharge.

- Gestion des ports https 443 et http 80 

-Redirection de toutes les demandes HTTP vers HTTPS en utilisant une réponse de redirection 301. 

-Reverse proxy pour gérer les requêtes HTTP vers le micro-service Flask et Drupal pour cacher notre infrastructure et améliorer la sécurité, la gestion des connexions et la flexibilité de notre infrastructure. 

-Configurer une zone de limitation de fréquence pour contrôler le nombre de requêtes par seconde que les adresses IP 

-Configurer des logs 

-Intégrer la mise en place des certificats SLL 

-Directives SSL pour améliorer la sécurité (optionnel mais recommandé)

- Limitation du nombre de requête sur un temps donné :
                                                      limit_req: Cela applique la limite définie précédemment dans la zone "one" dans le bloc LOCATION
                                                      burst: Cela spécifie le nombre de requêtes autorisées en rafale.
                                                      nodelay: Cela signifie que les requêtes en excès seront mises en file d'attente plutôt que rejetées immédiatement.

-Ajouter des en-têtes de sécurité pour renforcer la sécurité du serveur, y compris la politique de sécurité du contenu, la politique de transport strict, etc. 

-Vérifier l’utilisation de méthode de requête HTTP et retourner une réponse 405 (Méthode non autorisée) si elle n'est pas GET, HEAD ou POST. 

-Configurer la gestion de la taille du corps de la requête, des délais et des délais de réponse. 

-Configuration de la compression Gzip pour économiser la bande passante en compressant les données envoyées au client plus de charge pour le serveur mais requêtes plus rapides 
  



### Web application Firewall ou WAF : Intégration du module ModSecurity avec les règles Core Rules Set OSWAP

ModSecurity est un pare-feu d'application web (WAF) open source qui peut aider à protéger votre application web contre une variété d'attaques, y compris les injections SQL, les attaques par script entre sites (XSS), les tentatives d'exploitation de vulnérabilités et bien plus encore.

    - Protection avancée contre les attaques : Utilisation des règles de sécurité spécifiques pour identifier et bloquer les tentatives d'attaques web, offrant ainsi une couche de protection supplémentaire pour vos applications web. 

     - Détection en temps réel : Surveillance du trafic web entrant en temps réel et peut réagir rapidement aux menaces potentielles, ce qui permet de détecter et de bloquer les attaques dès qu'elles se produisent. 
 
    - Personnalisable : Possibilité de personnaliser les règles ModSecurity pour répondre aux besoins spécifiques de votre application web et de votre environnement. 
 
    - Audit et journalisation : ModSecurity génère des journaux détaillés des activités, ce qui facilite la détection et la résolution des incidents de sécurité. 
 
    - Prévention des vulnérabilités connues : En utilisant des règles de sécurité constamment mises à jour, ModSecurity peut aider à bloquer les attaques exploitant des vulnérabilités connues dans des applications web populaires. 
 
   - Protection contre les bots malveillants : pour aider à bloquer le trafic de bots malveillants qui tentent de scruter ou de perturber votre site web. 
 
    - Conformité aux normes de sécurité : L'ajout de ModSecurity peut contribuer à la conformité aux normes de sécurité telles que PCI DSS, HIPAA, et d'autres, en renforçant la sécurité de votre application web.


    
PARAMETRAGES DES FICHIERS :

    
Pour utiliser ModSecurity avec Nginx, nous devons installer le module ModSecurity pour Nginx et télécharger les règles ModSecurity à partir de sources telles que OWASP (Open Web Application Security Project :Core Rules Set ou CRS 3.3.5)
ou personnalisées en fonction des besoins de notre application, fichiers concernés :

### /etc/nginx/nginx.conf :

![My Image](/images/modsecurity_on.png)

#### /etc/nginx/modsec/main.conf : 
Ce fichier donne les paths des CRS 3.3.5 et du fichier principal de modSecurity.
Le chemin de ce fichier apparait également dans le fichier nginx.conf.

Include /etc/nginx/modsec/modsecurity.conf

Include /etc/nginx/modsec/coreruleset-3.3.5/crs-setup.conf

Include /etc/nginx/modsec/coreruleset-3.3.5/rules/*.conf 



#### /etc/nginx/modsec/modsecurity.conf :
Fichier de configuration principale de ModSecurity qui contient diverses directives qui définissent le comportement du pare-feu d'application web. 
 
Rule engine initialization  
SecRuleEngine O 

Request body handling 
SecRequestBodyAccess On

The location where ModSecurity stores temporary files 
SecTmpDir /tmp/

The location where ModSecurity will keep its persistent data. 
SecDataDir /tmp/

Maximum request body size we will accept for buffering. 
SecRequestBodyLimit 13107200 
SecRequestBodyNoFilesLimit 131072 
ETC  



#### /etc/nginx/modsec/unicode.mapping :
Le fichier Unicode Mapping est utilisé pour spécifier comment ModSecurity doit traiter les caractères Unicode dans les requêtes HTTP. Ce fichier de mappage est essentiel pour prendre en charge des encodages de caractères étendus et internationaux, garantissant que ModSecurity puisse détecter et bloquer les attaques qui utilisent ces encodages pour contourner les règles de sécurité. 



#### ngx_http_modsecurity_module.so 
Ce module Nginx permet d'intégrer ModSecurity dans le serveur web Nginx. Ce module étend les fonctionnalités de Nginx pour inclure des règles de sécurité avancées et la détection des attaques web. Il est souvent utilisé pour renforcer la sécurité des applications web hébergées sur des serveurs Nginx. 



#### Exemple de règle ModSecurity (custom) pour bloquer les tentatives d'injection SQL dans les paramètres d'URL :
SecRule ARGS "@rce" "id:1001,phase:2,deny,status:403,msg:'SQL Injection Attempt'"

Cette règle, lorsqu'elle est activée, surveille les paramètres d'URL (ARGS) à la recherche de la chaîne "@rce" (qui pourrait indiquer une tentative d'exécution de commande à distance) et, si elle la détecte, elle bloque la requête avec un code d'état HTTP 403 (Interdit) et enregistre un message dans les journaux.

![My Image](/images/Script_injection.png)



### Jenkins 
#### Dockerfiles

Les Dockerfiles permettent de construire les images Docker de jenkins, une pour le noeud controleur et une pour l'agent jenkins qui vas excuter le pipline, voici les principales étapes effectuées dans ces fichiers :

- Utilisation d'une image de base officielle de jenkins et jenkins agent.
- Installation des dépendances.
- Gestion des autorisations pour l'utilisateur Jenkins.
- Copie des fichiers pour les tests de charge.

#### charge.jmx
Ce fichier definit le test de charges qui sera réaliser dans la pipeline.
![jmeter](https://github.com/Sparkly74/ProjectBGroup2/assets/84808314/8f037a3b-8eec-41db-8bed-761767e32cfc)

### Configuration de jenkins 
activer les plugins suivant : 
- performence
- Docker
- HTML Publicher
- HTTP request
- Git

Crée les credentials suivant : 
- secret file pour le .env de drupal
- secret file pour le .env de micro service
- password pour le token gitHub
- SSH pour l'agent jenkins

Configurer le node de l'agent jenkins depuis l'interface administrer jenkins.

### La pipeline 
elle se trouve dans le jenkinsfile qui est lancer depuis jenkins.
elle : 
- verifie les bonnes pratiques de code 
- scanne la securité du code du micro service
- lance les tests unitaire
- en cas de succés elle lance le build puis le run de l'application
- à la fin deux options sont possible :
  - en cas de reussite un test de charge est effectuer un rapport de securité générer et le code est automatiqument push sur la branche last-stable de gitHub
  - en cas d'echec un rollback est effectuer afin d'annuler le deploielent en cours et deployer la branche last-stable.

Les rapports de test de charge et de securité sont ensuite disponible dans un onglet sur jenkins.

### Monitoring 

#### Prometheus

Système open-source de surveillance et d'alerte conçu pour collecter, stocker et analyser des métriques sur les systèmes informatiques, ici notre notre serveur gunicorn sur le port 9000

Prometheus se connecte aux metriques du micro service via le fichier prometheus.yml et permet de configurer des alertes, grace au fichier first_rules.yml.

Il est principalement utilisé pour surveiller la santé et les performances des applications et des infrastructures :
- Collecte des métriques activement en interrogeant notre serveur à intervalles réguliers. Ces cibles exposent leurs métriques via un point de terminaison HTTP appelé "endpoint 
- Stockage des métriques dans une base de données temps réel appelée "Time-Series Database".
- Possibilité de définir des règles d'alerte basées sur des métriques.



#### Grafana (en binôme avec Prometheus)

Grafana se connecte à prometheus et permet de créer des dashboards à partir des metriques recuperées.

- Visualisation et Tableaux de bord : Le rôle principal de Grafana est de permettre aux utilisateurs de créer des tableaux de bord personnalisés pour visualiser les données provenant de différentes sources, y compris Prometheus.
Grafana offre une interface utilisateur intuitive pour créer des graphiques, des jauges, des tableaux de bord, et plus encore. Les utilisateurs peuvent personnaliser ces tableaux de bord pour afficher les métriques spécifiques qui les intéressent.

- Interrogation des données : Grafana permet aux utilisateurs d'interroger les données stockées dans Prometheus à l'aide de son propre langage de requête.
On peutcréer des requêtes pour extraire des métriques spécifiques, appliquer des agrégations, filtrer les données et afficher les résultats dans des graphiques interactifs.

- Alerting : Grafana offre des fonctionnalités d'alerte qui permettent aux utilisateurs de définir des règles d'alerte basées sur les données Prometheus.
Lorsque les conditions spécifiées dans les règles d'alerte sont remplies, Grafana peut déclencher des alertes qui sont envoyées par e-mail, Slack, ou d'autres canaux de notification.



#### Alertmanager 

Envoie les alertes par Email

Exemple de setup de redirection d'alerte sur un email

![My Image](/images/alertsmanager.png)

![My Image](/images/Prometheus.png)



### Working in progress 

- Utilisation de OWASP ZAP 2.13.0 pour detecter les failles de securité.  https://www.zaproxy.org/

- Utilisation du Header Nginx https://securityheaders.com/ pour tester le filtrage des requêtes.
 
- Utilisation de NMAP pour scanner les ports de notre serveur Nginx.
 
- Utilisation de Fail2ban : Outil qui permet de faire un suivi des requêtes IP entrante FAILED arrivant sur notre serveur et de bannir les IP concernées à  
  partir de seuil que l'on définit en amont.

- Optimisation du fichier Nginx.conf :configurer une zone mémoire de cache pour réduire la charge du serveur (WORK IN PROGRESS)
 proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_temp_path=off

- Interface graphique
  
- load balancer

- Outil de détection de mise à jour des conteneurs comme Watchtower

- Radon afin d'analyser la complexité du code et les possibilité de refactorisation



  ### Difficultés rencontrées
  
  - Répartition des tâches au départ lié à la visibilité sur le projet
  
  - Développement du micro-service
  
  - Déploiement automatique de Drupal qui nécessite Drush (Drupal Shell)
  
  - Tentative de développement d'une interface graphique
  
  - Durée du projet : durée réduite pour la mise en place d'un tel projet. Beaucoup de temps passé sur le développement et moins sur la partie devops.


 




 



 




