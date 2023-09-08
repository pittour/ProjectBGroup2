# Use an official Drupal base image
FROM drupal:10.1.2-apache

# Install dependencies
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN groupadd -r apache && useradd -r -g apache apache

# Add Composer bin directory to PATH
ENV PATH="/root/.composer/vendor/bin:${PATH}"

# Copy your custom entry point script, php ini and ssl config
COPY entrypoint1.sh /usr/local/bin/entrypoint1.sh
COPY php.ini /usr/local/etc/php/php.ini
COPY default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf

# Make the script executable
RUN chmod +x /usr/local/bin/entrypoint1.sh
RUN chmod +x /usr/local/etc/php/php.ini

RUN chown -R apache:apache /var/run/apache2

# Set the working directory to Drupal web root
WORKDIR /opt/drupal
RUN chown -R apache:apache /opt/drupal

RUN composer self-update

RUN composer require drush/drush

RUN composer install

WORKDIR /etc/ssl
RUN openssl genrsa -out kprivkpub.key 2048
RUN openssl req -x509 -nodes -days 365 -key kprivkpub.key  -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt  -subj /C="FR"/ST="Rhone"/L="Lyon"/O="My Organization"/OU="My Unit"/CN="mydomain.com"/emailAddress="admin@mydomain.com"
RUN a2enmod ssl
RUN a2enmod headers
RUN service apache2 restart

RUN chown -R apache:apache /etc/ssl

USER apache

CMD ["/usr/local/bin/entrypoint1.sh"]