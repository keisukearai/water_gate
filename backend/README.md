### python version
python -V
Python 3.10.6

### python link
cd /usr/bin

ls -l | grep python

ln -s ./python3.8 ./python

# pip install
apt install -y python3-pip

### ipython etc
pip install ipython

apt -y install libmysqlclient-dev

apt-get install pkg-config

### mysql version
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash

curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --mariadb-server-version="mariadb-10.4"

### mysqlclient
pip install mysqlclient

### mariadb-server
##### apt install -y mariadb-server
apt-get install -y mariadb-server mariadb-client

# mysql
mysql

GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

create database wg_api_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

grant all on wg_api_db.* to 'admin'@'localhost';

### Django install
# python -m pip install Django

### make project
django-admin startproject admin_api

### make sub project
python manage.py startapp api

### runserver
python manage.py runserver

### migrate
python manage.py migrate

### createsuperuser admin
python manage.py createsuperuser

### makemigrations
python manage.py makemigrations api

python manage.py migrate

### nginx config
cd /etc/nginx/sites-available/

vi testapi.kotoragk.com

```config
server {
    client_max_body_size 64M;
    listen 80;
    server_name test.kotoragk.com www.test.kotoragk.com;

    location /admin {
        proxy_pass http://127.0.0.1:8000;
        proxy_read_timeout 60;
        proxy_connect_timeout 60;
        proxy_redirect off;

        # Allow the use of websockets
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /api {
        proxy_pass http://127.0.0.1:8000;
        proxy_read_timeout 60;
        proxy_connect_timeout 60;
        proxy_redirect off;

        # Allow the use of websockets
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    ・・・・
}
```

nginx -t

systemctl restart nginx

### admin site confirm
http://test.kotoragk.com/admin

### gunicorn
apt install gunicorn
python -m pip install gunicorn

### gunicorn start
gunicorn --bind 127.0.0.1:8000 admin_api.wsgi -D

### gunicorn stop
pkill gunicorn

### gunicorn status
ps aux | grep gunicorn

## db init

### table drop
use wg_api_db;
drop table watergate;
drop table area;
drop table prefecture;

### migrations file delete
rm -rf /root/water_gate/water_gate/backend/api/migrations/*.py

python manage.py migrate --fake api zero
python manage.py makemigrations api
python manage.py migrate

### data import
python manage.py loaddata master.json