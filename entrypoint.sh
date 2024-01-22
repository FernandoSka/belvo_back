#!/bin/bash

function run_app {
  echo "Initialiazing app ..."
  gunicorn --workers 3 --bind 0.0.0.0:8000 config.wsgi --timeout 300
}

function run_dev_app {
  echo "Initialiazing app ..."
  python manage.py runserver 0.0.0.0:8000
}

function run_debug_app {
  echo "Initialiazing app and waiting connection from debuger ..."
  python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000
}

#echo "Waiting for Database ..."
#python manage.py wait_for_db
#echo "Aplying migrations ..."
#python manage.py migrate
#echo "Creating services ..."
#python manage.py create_services
#echo "Creating groups ..."
#python manage.py create_groups
#echo "Creating admin user ..."
#python manage.py create_admin_user
#echo "Collecting statics ..."
#python manage.py collectstatic --noinput
#echo "Starting cron ..."
#service cron start
#echo "$SCHEDULER_FORMAT SCHEDULER_PASSWORD=$SCHEDULER_PASSWORD SCHEDULER_HOST=$SCHEDULER_HOST /usr/local/bin/python /code/core/cron.py >> /logs-tbi/logs.log 2>&1" | crontab -


#python manage.py loaddata instruccionfinanciera.json
#python manage.py loaddata instruccionfinancieraautomatica.json
#python manage.py loaddata instruccionfinancieraprevia.json
#python manage.py loaddata operacion.json
#python manage.py loaddata producto.json



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