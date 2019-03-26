#!/bin/bash

# Remove bloatware (Wolfram Engine, Libre Office, Minecraft Pi, sonic-pi dillo gpicview penguinspuzzle oracle-java8-jdk openjdk-7-jre oracle-java7-jdk openjdk-8-jre)
sudo apt remove --purge wolfram-engine libreoffice* scratch* minecraft-pi sonic-pi dillo gpicview oracle-java8-jdk openjdk-7-jre oracle-java7-jdk openjdk-8-jre -y

# Autoremove
sudo apt autoremove -y

# Clean
sudo apt autoclean -y

# Update
sudo apt update

# Upgrade
sudo apt upgrade -y

# Rpi-Update
sudo apt rpi-update -y

# LXML Requirements
sudo apt install libxml2-dev libxslt-dev python-dev -y

# Pip packages
sudo pip install pygame beautifulsoup4

# LXML
sudo apt install python-lxml -y

# UTF8 for Python
sudo nano /usr/lib/python2.7/sitecustomize.py

# Add the following to that ^
import sys
sys.setdefaultencoding('UTF8')