# Use an official Drupal base image
FROM drupal:10.1.2-apache

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Drush globally using Composer


# Add Composer bin directory to PATH
ENV PATH="/root/.composer/vendor/bin:${PATH}"

# Copy your custom entry point script
COPY entrypoint1.sh /usr/local/bin/entrypoint1.sh
COPY php.ini /usr/local/etc/php/php.ini

# Make the script executable
RUN chmod +x /usr/local/bin/entrypoint1.sh
RUN chmod +x /usr/local/etc/php/php.ini

# Set the working directory to Drupal web root
WORKDIR /opt/drupal

RUN composer self-update

RUN composer require drush/drush

RUN composer install

CMD ["/usr/local/bin/entrypoint1.sh"]