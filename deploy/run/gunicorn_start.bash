#!/bin/bash

NAME="lum"                                  # Name of the application
DJANGODIR=/webapps/lum             # Django project directory
SOCKFILE=/webapps/lum/deploy/run/gunicorn.sock  # we will communicte using this unix socket
USER=deploy                                      # the user to run as
GROUP=deploy                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=settings.dev            # which settings file should Django use
DJANGO_WSGI_MODULE=lum.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/deploy/.virtualenvs/lum/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/deploy/.virtualenvs/lum/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
