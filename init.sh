#!/bin/sh
sudo /etc/init.d/mysql restart
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf 
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES"
/home/box/web/ask/manage.py syncdb