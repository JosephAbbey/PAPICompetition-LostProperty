#!/bin/sh

# Install required packages
sudo apt-get install nginx
sudo apt-get install python3-pip

# Install uwsgi
sudo pip3 install uwsgi

# Install the actual LostProperty system
sudo chown www-data LostProperty/
sudo python3 LostProperty/install.py