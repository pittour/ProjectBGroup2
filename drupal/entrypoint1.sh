#!/bin/bash

# Waiting for mysql container to be setup
echo "Waiting for mysql container..."

# Changer de méthode. Requete http ?
sleep 25

cd /opt/drupal

# Perform Drupal site installation using Drush
drush site-install demo_umami --account-pass=${DRUPAL_PASSWORD} --db-url=mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@mysql/${MYSQL_DATABASE} -y

# Installs modules
drush pm:install jsonapi
drush pm:install basic_auth
drush config:delete jsonapi.settings read_only

apache2-foreground