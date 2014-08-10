#!/bin/bash
sudo apt-get -y upgrade
sudo apt-get -y update

# install python
sudo apt-get -y install python2.7

# install pip and virtualenv
sudo apt-get -y install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install virtualenv
sudo pip install --upgrade virtualenv


# install dependencies for postgres to work with django
sudo apt-get -y install libpq-dev
# install postgreSQL
sudo apt-get -y install postgresql postgresql-contrib


# install sqlite3
sudo apt-get -y install sqlite3

# install git
sudo apt-get -y install git

# install nginx
sudo apt-get -y install nginx

# grab the TownHall git project files
git clone https://github.com/DanielPorter/TownHall.git
cd TownHall

# make a new virtual environment
virtualenv venv

# activate that venv!
. venv/bin/activate

# backend for PostgreSQL
pip install psycopg2

# These guys get installed with Django I think
# but here is installing them first
pip install Jinja2 ##
pip install Werkzeug ##
pip install gunicorn ## install Python WSGI HTTP server
pip install itsdangerous ##
pip install markupsafe ##

# install Django
pip install Django==1.6.5

#install Django REST framework
pip install djangorestframework
pip install markdown
pip install django-filter

#install Django treebeard
pip install django-treebeard

# install pyparsing dependency for css
pip install pyparsing==2.0.2
# install python-scss
pip install scss
#install python scss compiler
pip install pyScss

# create psql database, user and privileges
sudo -u postgres psql -c "CREATE DATABASE townhall"
sudo -u postgres psql -c "CREATE USER usr WITH PASSWORD 'password'"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE townhall to usr;"

# install OAuth which handles specific authorization flows
pip install django-oauth2-provider==0.2.6.1

#cd ./TownHall
python manage.py syncdb --noinput

# set up and start nginx !
sudo cat server.txt > /etc/nginx/sites-available/TownHall
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/TownHall
sudo rm default
sudo service nginx start

#start the server!
cd ~/TownHall/
gunicorn -b 0.0.0.0:8000 TownHall.wsgi:application &
