#!/bin/bash

#Run migrations
python manage.py migrate

#start gunicorn
gunicorn learning_log.wsgi:applicationS