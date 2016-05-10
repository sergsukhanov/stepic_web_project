sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -uroot -e "create database qa"
#gunicorn -b 0.0.0.0:8080 hello:app
#./script.sh
