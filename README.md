# NLPP
Woooo, you have located the github page!

To use this Python 3 project the following MUST be installed with pip (or pip3) on your computer 
[use the format pip install package-name]

  	Django                  (The backend framework for site)
  	pillow                  (Helps with images)
	bcrypt                  (Better hashing)
	django[argon2]		(Better hashing)
	django-braces           (Better Template Tagging)
	django-bootstrap4       (Better Styling of Built in Django Forms
 	misaka                  (Allows for easier HTML storage in the database [such as markdown to html])
	django-debug-toolbar    (Easier to debug)
	djangorestframework	(Allows for us to make a custom api)
	requests		(Allows to send an http request from python app [used for APIs])
	django-clear-cache	(Quickly clears the session without needing settings.py path to be set]
	django-bleach 		(Escape HTML, regulate parameters, regulate styles, regulate protocols, etc.) 
	
 # Quickstart
 To run the server, navigate into the same level as manage.py and type in the commandline python manage.py runserver
 To acess the ip:port/admin page to view the databases, create a super user with the python manage.py createsuperuser command
 After adding a model, first do python manage.py makemigrations and then python manage.py migrate
 
# Accessing the Website
The website can found using [bit.ly/brom-nlpp](https://bit.ly/brom-nlpp)

The website itself can be updated using a shared bash, email me for the link.
To update the site if there is a new version of github go the ~/NLPP/NLPP (but not ~/NLPP/NLPP/NLPP) and then
1. `git pull`
	* If there is a merge conflict, then use `git reset --hard`, but be aware that this will overide all files on the site, so don't do this in production

2. `touch /var/www/alearningcurve_pythonanywhere_com_wsgi.py`     
	* this command will restart the webserver, but it will take a few seconds, so be patient!
