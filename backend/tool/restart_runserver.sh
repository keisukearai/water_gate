ps aux | grep runserver | grep -v grep | awk '{ print "kill -9", $2 }' | sh
/usr/bin/python /var/www/html/water_gate/backend/manage.py runserver 127.0.0.1:8000 --insecure &