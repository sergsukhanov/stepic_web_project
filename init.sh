#!/bin/sh
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf 
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE db_stepic_project;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'django';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON db_stepic_project.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
/home/box/web/ask/manage.py syncdb
sudo rm /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -uroot -e "create database qa"