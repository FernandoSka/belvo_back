#!/bin/bash

function run_app {
  echo "Initialiazing app ..."
  gunicorn --workers 3 --bind 0.0.0.0:8000 belvo.wsgi --timeout 300
}

function run_dev_app {
  echo "Initialiazing app ..."
  python manage.py runserver 0.0.0.0:8000
}

function run_debug_app {
  echo "Initialiazing app and waiting connection from debuger ..."
  python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000
}

echo "Aplying migrations ..."
python manage.py migrate
python manage.py create_admin_user
echo "Collecting statics ..."
python manage.py collectstatic --noinput



if [ "$ENV" == "PROD" ] 
then
  run_app
elif [ "$ENV" == "DEBUG" ]
then
  run_debug_app
else
  run_dev_app
fi

while true
do
  sleep 20
done