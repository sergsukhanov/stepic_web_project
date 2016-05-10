#!/bin/bash
set -e
LOGFILE=/home/box/web/log/gunicorn/ask.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=box
GROUP=box
PORT=8000 # Этот порт будет разным у каждого django-проекта
cd /home/box/web/ask
#exec workon stepic_web_project
#stepic_web_project -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE \
  --bind 0.0.0.0:$PORT
