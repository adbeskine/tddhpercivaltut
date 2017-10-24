Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* Git

eg, on Ubuntu:
	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get install nginx
	sudo apt-get install git
	sudo apt-get install python36
	sudo apt-get install python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with desired sitename

## Folder structure:
Assume we have a user account at /home/username

/home/username
|---sites
	   |---SITENAME
	          |---database
	          |---source
	          |---static
	          |---virtualenv