#!/bin/bash
sudo apt-get update
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi python-dev -y
apt-get install python-pymysql -y
apt-get install python-sqlalchemy -y
apt-get install python-mysqldb -y
sudo a2enmod wsgi 
cd /var/www
mkdir FlaskApp
cd FlaskApp
mkdir FlaskApp
cd FlaskApp
sudo mkdir static templates
touch __init__.py
echo 'from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    app.run()' >> __init__.py
sudo apt-get install python-pip 
sudo pip install virtualenv 
sudo virtualenv venv
source venv/bin/activate 
sudo pip install Flask sqlalchemy
deactivate
sudo touch /etc/apache2/sites-available/FlaskApp.conf

echo '<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>'' >> /etc/apache2/sites-available/FlaskApp.conf
sudo a2ensite FlaskApp
cd /var/www/FlaskApp
sudo touch flaskapp.wsgi
echo '#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = "BoooHooo"' >> flaskapp.wsgi 
sudo service apache2 restart 
echo "Installing MySQL... standby to set root Password"
sudo apt-get install mysql-server -y
echo "COMPLETED"

