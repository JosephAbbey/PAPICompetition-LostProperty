#!/bin/sh

# Install required packages
sudo apt-get install nginx
sudo apt-get install python3-pip

# Install uwsgi
sudo pip3 install uwsgi

# Install the actual LostProperty system
sudo python3 ./install.py
sudo chmod -R a+rwx ./