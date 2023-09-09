FROM python:slim-bullseye

RUN apt-get update && \
    apt-get clean && \
    apt-get install -y nginx && \
    apt-get install -y redis && \
    apt install -y wget && \
    apt install -y git

RUN apt-get install -y ufw

### FIREWALLING SETUP ###
RUN ufw allow 80/tcp
RUN ufw allow 443/tcp
RUN ufw allow 8000/tcp

RUN ufw default deny incoming
RUN ufw default allow outgoing

RUN ufw logging on
RUN ufw logging medium
RUN service ufw start

########################

WORKDIR /etc/ssl
RUN openssl genrsa -out kprivkpub.key 2048
RUN openssl req -x509 -nodes -days 365 -key kprivkpub.key -out /etc/ssl/certs/nginx-selfsigned.crt  -subj /C="FR"/ST="Rhone"/L="Lyon"/O="My Organization"/OU="My Unit"/CN="mydomain.com"/emailAddress="admin@mydomain.com"

WORKDIR /drupal-brutal
ENV PROMETHEUS_MULTIPROC_DIR /tmp
ENV prometheus_multiproc_dir /tmp

COPY . .

# ##################### NGINX CONFIGURATION + MODSECURITY + CRS 3.3.5 ##############################
COPY nginx.conf /etc/nginx/nginx.conf
RUN apt update && mkdir modsecu && cd modsecu && wget https://nginx.org/download/nginx-1.18.0.tar.gz && wget https://github.com/SpiderLabs/ModSecurity/releases/download/v3.0.10/modsecurity-v3.0.10.tar.gz && tar -zxvf nginx-1.18.0.tar.gz && tar -zxvf modsecurity-v3.0.10.tar.gz &&   apt-get install -y gcc make automake autoconf libtool libpcre3 libpcre3-dev libxml2 libxml2-dev apache2-dev apt-utils build-essential git libcurl4-openssl-dev libgeoip-dev liblmdb-dev libpcre++-dev pkgconf wget zlib1g-dev && cd modsecurity-v3.0.10 && ./configure --enable-standalone-module && make -j8 && make install && cd .. && git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && cd nginx-1.18.0 && ./configure --with-compat --add-dynamic-module=../ModSecurity-nginx/ && make -j8 && make modules && cp objs/ngx_http_modsecurity_module.so /etc/nginx/modules-available/ && ln /etc/nginx/modules-available/ngx_http_modsecurity_module.so /etc/nginx/modules-enabled/ && ln /etc/nginx/modules-available/ngx_http_modsecurity_module.so /usr/share/nginx/modules/

RUN mkdir /etc/nginx/modsec/
COPY main.conf /etc/nginx/modsec/main.conf
COPY modsecurity.conf /etc/nginx/modsec/modsecurity.conf
COPY unicode.mapping /etc/nginx/modsec/unicode.mapping

RUN wget https://github.com/coreruleset/coreruleset/archive/refs/tags/v3.3.5.tar.gz
RUN tar -xvf v3.3.5.tar.gz

RUN cp -r coreruleset-3.3.5 /etc/nginx/modsec/
RUN mv /etc/nginx/modsec/coreruleset-3.3.5/crs-setup.conf.example /etc/nginx/modsec/coreruleset-3.3.5/crs-setup.conf


##################################################################################################

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
CMD ["sh", "-c", "redis-server & gunicorn -c config-gunicorn.py --bind 0.0.0.0:8000 app:app & nginx -g 'daemon off;'"]