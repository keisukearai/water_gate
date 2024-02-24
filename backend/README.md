### python version
python3 -V
Python 3.10.6

### python link
cd /usr/bin

#### version確認
ls -l | grep python
#### link削除
rm -rf /usr/bin/python
#### 再link
ln -s ./python3.10 ./python

### python version
python -V

# pip install
apt install -y python3-pip

### ipython etc
pip install ipython

apt -y install libmysqlclient-dev

apt-get install pkg-config

apt install -y cron

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
#python -m pip install Django

### make project
#django-admin startproject admin_api

### make sub project
#python manage.py startapp api

### requirements
cd /var/www/html/watar_gate/backend
#python -m pip install -r requirements.txt
python -m pip install django==4.2.5
python -m pip install django-cors-headers
python -m pip install mysqlclient
python -m pip install python-dotenv
python -m pip install Pillow
python -m pip install django-resized

### runserver
python manage.py runserver

### logsディレクトリ作成
mkdir logs

### migrate
python manage.py makemigrations api
python manage.py migrate

### createsuperuser admin
python manage.py createsuperuser

### nginx config
cd /etc/nginx/sites-available/

vi testapi.kotoragk.com

```config
server {
    client_max_body_size 64M;
    listen 80;
    server_name test.kotoragk.com www.test.kotoragk.com;

    location ~ (/admin|/api) {
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

    location /media  {
        alias /var/www/html/water_gate/backend/media; # Absolute path.
    }

    ・・・・
}
```
### 構文チェック
nginx -t

### リスタート
systemctl restart nginx

### ALLOWED_HOSTS設定
cd /var/www/html/backend
vi admin_api/settings.py

### admin site confirm
https://test.kotoragk.com/admin

### gunicorn 実施しない
#apt install gunicorn
#python -m pip install gunicorn

### gunicorn start 実施しない
#gunicorn --bind 127.0.0.1:8000 admin_api.wsgi -D --insecure

### gunicorn stop 実施しない
#pkill gunicorn

### gunicorn status 実施しない
#ps aux | grep gunicorn

### runserver
python manage.py runserver 127.0.0.1:8000 --insecure &

ps aux | grep runserver
kill -9 %1

## db init

### table drop
use wg_api_db;
drop table wg_gateway_json_data;
drop table wg_end_device_data;
drop table wg_end_device;
drop table wg_gateway;
drop table wg_area;
drop table wg_prefecture;
drop table wg_status_info;
drop table wg_class_info;
drop table wg_system_info;

truncate table wg_base
truncate table wg_area
truncate table wg_prefecture
delete from wg_prefecture

### migrations file delete
rm -rf ./api/migrations/*.py
rm -rf /root/water_gate/water_gate/backend/api/migrations/*.py
rm -rf /var/www/html/water_gate/backend/api/migrations/*.py

python manage.py migrate --fake api zero
python manage.py makemigrations api
python manage.py migrate

### data import
python manage.py loaddata master.json
python manage.py loaddata master_gate_data.json
python manage.py loaddata gate_data.json

### local url
http://localhost:8000/admin/

# git rest
git fetch origin main
git reset --hard origin/main

# nginx 502エラー画面
vi /var/www/html/custom_50x.html

cd /etc/nginx/sites-available/

vi testapi.kotoragk.com

```config
server {
    ・・・・

    location /media  {
        alias /var/www/html/water_gate/backend/media; # Absolute path.
    }

    error_page 500 502 503 504 /500.html;
    location = /500.html {
        root /var/www/html/water_gate/backend/templates;
        internal;
    }

    ・・・・
}
```

### 構文チェック
nginx -t

### リスタート
systemctl restart nginx

## certbot renew
root

mkdir -p .well-known/acme-challenge

vi /etc/nginx/sites-enabled/test.kotoragk.com

listen 80;

location ^~ /.well-known/acme-challenge/ {
    default_type "text/plain";
    root /root;
}

### fw
ufw allow 80

### cron
certbot renew

00 02 01 * * certbot renew && systemctl restart nginx


### Basis認証
#### アプリインストール
apt-get install apache2-utils

#### 認証情報の設定
htpasswd -c /etc/nginx/sites-available/.htpasswd admin

vi /etc/nginx/sites-enabled/test.kotoragk.com

location / {
    auth_basic "Login Authentication"; # 認証時に表示されるメッセージ
    auth_basic_user_file /etc/nginx/sites-available/.htpasswd; # .htpasswdファイルのパス
}

#### 構文チェック
nginx -t

#### リスタート
systemctl stop nginx
systemctl start nginx