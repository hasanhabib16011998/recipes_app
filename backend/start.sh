#!/bin/sh

# Apply database migrations
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Start Django server
python -m dotenv -f .env manage.py runserver 0.0.0.0:8000
