# ProjectBGroup2 : Kevin, Hadi, Christophe


# JOURNAL DE BORD


# OBJECTIF: Transformer une application monolithique en micro-services

 ---------------------------------------------------------------------------------------------------------------------------------
# JOUR 1 :


## I ) APPLICATION MONOLITHIQUE VERSUS APPLICATION EN MICRO-SERVICES


### 1) Qu’est ce que l’architecture monolithique ?

### 2) Quels sont les points forts de l’architecture monolithique?

### 3) Quelles sont les faiblesses de l’architecture monolithique ?

### 4) Qu’est ce que l’architecture de microservices ? 

### 5) Quels sont les points forts de l’architecture de microservices ? 

### 6) Quelles sont les faiblesses de l’architecture de microservices ? 

### 7) Microservices et architecture monolithique : Quelle est la différence ?

 
### 1 ) Qu’est ce que l’architecture monolithique ? 

L’architecture monolithique est considérée comme une manière traditionnelle de construire des applications. Une application monolithique est construite comme une unité unique et indivisible. Habituellement, une telle solution comprend une interface utilisateur côté client, une application côté serveur et une base de données. Elle est unifiée et toutes les fonctions sont gérées et servies en un seul endroit.

Normalement, les applications monolithiques ont une seule grande base de code et manquent de modularité. Si les développeurs veulent mettre à jour ou modifier quelque chose, ils accèdent à la même base de code. Ils apportent donc des modifications à l’ensemble de la stack en une seule fois.

 
### 2 ) Quels sont les points forts de l’architecture monolithique? 

Moins de problèmes transversaux

Les préoccupations transversales sont celles qui affectent l’ensemble de l’application, comme la journalisation, la manipulation, la mise en cache et le contrôle des performances. 

Dans une application monolithique, ce domaine de fonctionnalité ne concerne qu’une seule application, il est donc plus facile de le gérer.
 
Débogage et tests plus faciles

Contrairement à l’architecture microservices, les applications monolithiques sont beaucoup plus faciles à déboguer et à tester. Puisqu’une application monolithique est une unité unique et indivisible, vous pouvez effectuer des tests de bout en bout beaucoup plus rapidement.

 
Simplicité de déploiement

Un autre avantage associé à la simplicité des applications monolithiques est la facilité de déploiement. Avec les applications monolithiques, vous n’avez pas à gérer de nombreux déploiements, mais seulement un fichier ou un répertoire.

 
Simplicité de développement

Tant que l’approche monolithique est une méthode standard de création d’applications, toute équipe d’ingénieurs dispose des connaissances et des capacités nécessaires pour développer une application monolithique.

 
### 3 ) Quelles sont les faiblesses de l’architecture monolithique ? 
La compréhension

Lorsqu’une application monolithique évolue, elle devient trop compliquée à comprendre. En outre, un système complexe de code au sein d’une application est difficile à gérer.

 
Apporter des modifications

Il est plus difficile de mettre en œuvre des changements dans une application aussi vaste et complexe avec un couplage très étroit. Toute modification du code affecte l’ensemble du système et doit donc être minutieusement coordonnée. Cela rend le processus de développement global beaucoup plus long.

 
L’évolution

Il n’est pas possible de faire évoluer les composants de manière indépendante, mais uniquement l’application dans son ensemble.

 
Les obstacles liés aux nouvelles technologies

Il est extrêmement difficile d’appliquer une nouvelle technologie à une application monolithique, car il faut alors réécrire l’ensemble de l’application.

 
### 4 ) Qu’est ce que l’architecture microservices ? 

Alors qu’une application monolithique est une seule unité unifiée, une architecture microservices la décompose en un ensemble de petites unités indépendantes. Ces unités exécutent chaque processus d’application comme un service distinct. Ainsi, tous les services possèdent leur propre logique et leur propre base de données et exécutent les fonctions spécifiques.

 

Dans une architecture microservices, l’ensemble de la fonctionnalité est divisé en modules déployables indépendamment qui communiquent entre eux par le biais de méthodes définies appelées API (Application Programming Interface). Chaque service couvre sa propre portée et peut être mis à jour, déployé et mis à l’échelle indépendamment.

 
#### a ) Quels sont les points forts de l’architecture microservices ? 
Composants indépendants

Premièrement, tous les services peuvent être déployés et mis à jour indépendamment, ce qui donne plus de flexibilité. Deuxièmement, un bogue en microservices n’a d’impact que sur ce service particulier et n’influence pas l’ensemble de l’application. Enfin, il est beaucoup plus facile d’ajouter de nouvelles fonctionnalités à une application microservices qu’à une application monolithique.

 
Une compréhension plus aisée

Divisée en composants plus petits et plus simples, une application microservice est plus facile à comprendre et à gérer. Il suffit de se concentrer sur un service spécifique lié à un objectif commercial que vous avez.

 
Meilleure évolutivité

Un autre avantage de l’approche microservices est que chaque élément peut être mis à l’échelle indépendamment. L’ensemble du processus est donc plus rentable et plus rapide qu’avec les monolithes, où l’application entière doit être mise à l’échelle même si elle n’en a pas besoin. En outre, chaque monolithe a des limites en termes d’évolutivité, de sorte que plus le nombre d’utilisateurs augmente, plus le monolithe pose des problèmes. Par conséquent, de nombreuses entreprises finissent par reconstruire leurs architectures monolithiques.

 
Flexibilité dans le choix de la technologie

Les équipes d’ingénieurs ne sont pas limitées par la technologie choisie dès le départ. Elles sont libres d’appliquer diverses technologies et frameworks pour chaque microservice.

 
Le niveau supérieur d’agilité

Toute défaillance dans une application microservices n’affecte qu’un service particulier et non l’ensemble de la solution. Ainsi, tous les changements et toutes les expériences sont mis en œuvre avec moins de risques et moins d’erreurs.

  
#### b ) Quelles sont les faiblesses de l’architecture microservices ?

 
Une complexité supplémentaire

Une architecture de microservices étant un système distribué, vous devez choisir et configurer les connexions entre tous les modules et bases de données. En outre, tant qu’une telle application comprend des services indépendants, ils doivent tous être déployés indépendamment.

 
Distribution du système

Une architecture de microservices est un système complexe composé de plusieurs modules et bases de données, toutes les connexions doivent donc être gérées avec soin.

 
Préoccupations transversales

Lors de la création d’une application microservices, vous devrez gérer un certain nombre de problèmes transversaux. Il s’agit notamment de la configuration externalisée, de la journalisation, des métriques, des contrôles de santé, etc.

 
Test

Une multitude de composants déployables indépendamment rend le test d’une solution basée sur les microservices beaucoup plus difficile.

 
### 7 ) Microservices vs architecture monolithique : Quelle est la différence ?

Nous analyserons la complexité, la fiabilité, la latence et l’évolutivité de l’architecture monolithique par rapport aux microservices afin de mieux comprendre les différences.

 
Évolutivité

Les microservices ne sont pas les seuls à être évolutifs. Un monolithe peut également être mis à l’échelle. Toutefois, les applications monolithiques peuvent être mises à l’échelle dans une seule dimension et en exécutant plusieurs copies. Avec un volume de données croissant, vous ne serez pas en mesure de les faire évoluer. Une application microservices peut donc évoluer avec moins de ressources, ce qui est un avantage absolu des microservices.

 
Complexité

Les microservices impliquent une pléthore de codes sources, de frameworks et de technologies en fonction de la complexité de votre application. Plusieurs serveurs peuvent héberger les services, qui communiquent entre eux via des API.

 

L’architecture de ce type nécessite une méthodologie de développement différente et exige un niveau plus élevé de coordination, de compétences et de compréhension de l’architecture globale.

 
Latence

La latence d’une entité fait référence au temps qui s’écoule entre la stimulation et la réponse qui se produit après un certain changement physique. Les microservices sont principalement concernés par ce phénomène. Un microservice envoie ou reçoit des données en octets sur le réseau lorsqu’il communique avec un autre service. Les octets deviennent des signaux électriques, qui redeviennent des octets.

 

Les monolithes, en revanche, ne connaissent pas de latence réseau puisque tous les services sont situés dans le même flux de travail. Pour ces raisons, les microservices sont plus lents que les monolithes.

 
Fiabilité

Un monolithe se compose d’un seul serveur où se déroulent tous les appels et processus. En d’autres termes, si le réseau tombe en panne, c’est toute l’application qui s’arrête. En revanche, les appels réseau des microservices sont fiables à 99,9 %. Lorsqu’un des microservices tombe en panne, l’isolation des erreurs, une autre fonctionnalité des microservices, vous permet de maintenir l’application.

---------------------------------------------------------------------------------------------------------------------------------

[From Monolith to Microservices: A Guide To Replatforming](https://fabric.inc/blog/commerce/from-monolith-to-microservices)


---------------------------------------------------------------------------------------------------------------------------------

## II ) CHOIX DE L'APPLICATION CMS A MIGRER : DRUPAL

## 1 ) ANALYSE DE L'ARCHITECTURE EXISTANTE

Image docker: docker pull drupal:7.98-php8.2-fpm-bullseye



## 2 ) IDENTIFICATION DES DIFFERENTES FONCTIONNALITES MIGRABLES :
### 1- Gestion d'utilisateurs et d'authentification :
      Créer un micro-service pour gérer l'authentification, l'inscription des utilisateurs et la gestion des profils. Cela 
      pourrait permettre aux utilisateurs de s'authentifier de manière centralisée, même si d'autres parties de l'application 
      sont déployées en micro-services distincts.
### 2- Notifications : 
       Créer un micro-service pour gérer l'envoi de notifications par e-mail, SMS ou d'autres canaux.
### 3- Analyse et suivi :
       Créer un micro-service pour collecter et analyser les données de suivi et les statistiques d'utilisation.
