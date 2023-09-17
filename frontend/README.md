This is a [Next13.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## npm install
npm install --force

chmod 700 ./tool/build.sh

./tool/build.sh

## google map install [参考情報](https://dany-rivera.medium.com/how-to-add-google-maps-api-in-next-js-13-step-by-step-c027813d5769)
npm install --save google-maps-react --force

## flowbite install
npm install flowbite flowbite-react --save

## swr install
npm install swr

## mobie install
npm install react-device-detect --force

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Ubuntu 20.2[url](https://www.slingacademy.com/article/how-to-deploy-a-next-js-app-on-ubuntu-with-nginx-and-lets-encrypt/)
### update
apt-get update

### add user
adduser admin

### sudo
gpasswd -a admin sudo

### ufw
sudo ufw status

sudo ufw allow 80

sudo ufw reload

sudo ufw status

### install nginx
apt install -y nginx

### nginx staus [URL](http://118.27.19.113)
systemctl status nginx

systemctl enable nginx

### npm install
sudo apt install -y npm

### npm latest
sudo npm install -g n

# sudo n stable

# sudo apt purge nodejs npm

# suto apt autoremove

n v16.19.1

npm -v

8.19.3

node -v

v16.19.1

### chmod html
sudo chmod 777 -R /var/www/html/

### confirm
curl http://localhost:3000

### nginx config
ls -lt /etc/nginx/sites-enabled

rm /etc/nginx/sites-enabled/default

cd /etc/nginx/sites-available/

vi test.kotoragk.com

```config
server {
    client_max_body_size 64M;
    listen 80;
    server_name test.kotoragk.com www.test.kotoragk.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
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
}
```

ln -s /etc/nginx/sites-available/test.kotoragk.com /etc/nginx/sites-enabled/

nginx -t

systemctl restart nginx

### git config
git config --global user.name "keisukearai"

git config --global user.email "hoge@hoge.com"

#### git access token
git config credential.helper 'cache --timeout=86400'

### git clone
cd /var/www/html

git clone https://github.com/keisukearai/water_gate.git

### deplopy
cd /var/www/html/water_gate

npm install --force

#### env (see error url](https://stackoverflow.com/questions/76543198/error-while-deploying-next-js-app-on-vercel)
vi .env.local

npm run build

npm run start

### mp2 install
sudo npm install pm2 -g

pm2 start npm --name "water_gate" -- start

pm2 stop water_gate

pm2 status

### site confirm
http://test.kotoragk.com

### cerbot
apt install -y certbot python3-certbot-nginx

### cerbot setting
certbot --nginx -d test.kotoragk.com -d www.test.kotoragk.com

### ufw delete & add
ufw status numbered

ufw delete 2

ufw allow 443

### site confirm
https://test.kotoragk.com