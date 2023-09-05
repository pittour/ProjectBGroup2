FROM python:slim-bullseye

RUN apt-get update && \
    apt-get clean && \
    apt-get install -y nginx && \
    apt-get install -y redis

WORKDIR /etc/ssl
RUN openssl genrsa -out kprivkpub.key 2048
RUN openssl req -x509 -nodes -days 365 -key kprivkpub.key -out /etc/ssl/certs/nginx-selfsigned.crt  -subj /C="FR"/ST="Rhone"/L="Lyon"/O="My Organization"/OU="My Unit"/CN="mydomain.com"/emailAddress="admin@mydomain.com"

WORKDIR /drupal-brutal

COPY . .

RUN mv default /etc/nginx/sites-enabled/default
RUN mv nginx.conf /etc/nginx/nginx.conf

RUN pip3 install -r requirements.txt

EXPOSE 80
EXPOSE 443

RUN groupadd -r nginx && useradd -r -g nginx nginx

RUN chown -R nginx:nginx /drupal-brutal && chmod -R 755 /drupal-brutal && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d && \
        chown -R nginx:nginx /var/lib/nginx && \
        chown -R nginx:nginx /etc/ssl
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

USER nginx
CMD ["sh", "-c", "redis-server & gunicorn app:app --bind 0.0.0.0:8000 & nginx -g 'daemon off;'"]