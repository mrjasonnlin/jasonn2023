#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
#!python manage.py makemigrations
python manage.py migrate

# Create a superuser (non-interactive example)
# echo "from django.contrib.auth import get_user_model; \
# User = get_user_model(); \
# User.objects.create_superuser('admin', 'admin@gmail.com', 'admin11111')" | python manage.py shell

# echo "Setup complete! Superuser created with username: admin and password: admin11111"

