FROM python:slim-bullseye

RUN apt-get update && \
    apt-get clean && \
    apt-get install -y nginx

WORKDIR /drupal-brutal

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]