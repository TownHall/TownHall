#!/bin/bash
sudo apt-get -y upgrade
sudo apt-get -y update

# install python
sudo apt-get -y install python2.7

# install pip and virtualenv
sudo apt-get -y install python-pip python-dev build-essential 
sudo pip install virtualenv
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

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

# These guys get installed with Django I think
# but here is installing them first
pip install Jinja2  ##
pip install Werkzeug  ##
pip install gunicorn  ##
pip install itsdangerous  ##
pip install markupsafe  ##

# install Django
pip install Django==1.6.5

#install Django REST framework
pip install djangorestframework
pip install markdown
pip install django-filter

#install Django treebeard
pip install django-treebeard

#cd ./TownHall
python manage.py syncdb --noinput
