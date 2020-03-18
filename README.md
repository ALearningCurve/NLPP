# Natural Language Processing (NLPP)
Woooo, you have located the github page! This is a collaborative project to enhance the reading and learning experience of other languages. By adopting a format similiar to google classroom, student can easily join classrooms (called groups) and teachers can easily make them. The groups allow teachers to assign readings (and in later versions perhaps videos) where students can interact with the text to get a synomyn of that word in the target language the teacher specified before getting a translation after another succesive click. The program will keep track of the students' clicks and allow the teacher to see what words he/she might need to spend more time with on the class. With built in image, pdf, and word document text extraction the program strives to be as user friendly for teachers to upload resources

This site is not yet fully secured and as such deployment should involve a cautious approach. That being said, the site utilizes log in required checks for most pages, a secure hashing alogrithem, cross-site scripting (CXX) protection by escaping HTML (and using Django-Bleach to ensure fields that have HTML can not be taken advantage of), form validation to ensure that data is properly entered, and checks user against the owner of a post or group to prevent malicious actions.

# Installing the Code and External Resources
The project requires Python 3 and the following MUST be installed with pip (or pip3) on your computer 
with the command `pip3 install package-name`. There is also a requirements.txt that can be quickly installed with 
```
pip3 install -r requirements.txt 
pip3 freeze > requirements.txt
```
The list is here if you want to use another method as well as with descriptions of how we used them in our project:
```
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
nltk			(PDF Extraction - nltk.corpus and nltk.tokenize downloaded with "nltk.download("name")")
PyPDF2			(PDF Extraction)
textract		(PDF Extraction)
pytesseract		(Image Text Extraction)
mammoth			(Convert Word Documents into HTML)
```
This project also uses [Bootstrap4](https://getbootstrap.com/) to speed up the development process and enhance the user experience. It also uses the [TinyMCE API](https://www.tiny.cloud/docs/) to allow for easy and simple styling for user generated content. In terms of getting translations, it uses the [Yandex Translation API](https://tech.yandex.com/translate/) (as it free) and provides a link to [Google Translate](https://translate.google.com/) (which could not be used as an API due to it costing money). Due to experimentation, when the final Synomyn API is chosen it will be put here.

 # Quickstart
 To run the server, navigate into the same level as manage.py and type in the terminal `python manage.py runserver`. To run the server on a specific ip and port, use the command `python manage.py runserver 0.0.0.0:8888` in the format host:port. To acess the admin page to view the databases you must have a superuse account: create a super user with the `python manage.py createsuperuser` command and follow the steps prompted in the terminal. After adding a model (or changing its fields), first run `python manage.py makemigrations` and then `python manage.py migrate` to update the database with the alterations. After running migrations and having a super user account, to view or manually alter the database go to http://0.0.0.0/admin (where 0.0.0.0 is the actual host of the site) where you can login to see the tables.

Breif explanation of each table:
 * User: The accounts of the people on the site
 * Groups: The google classroom equivalent that details users and tracks which students are in the group and who has is the owner of the group.
 * Posts: The posts that are in each group that have the uploaded resources and attributes like due dates, students who have completed it, post creator, text, etc.
 * SupportedLanguages: Specify to the translation api what laguage is being used and what langauges the posts can be made in

 
# Acessing the Website
The website can found at [https://alearningcurve.pythonanywhere.com/](https://alearningcurve.pythonanywhere.com) or with [bit.ly/brom-nlpp](https://bit.ly/brom-nlpp)

The website itself can be updated using a shared bash, email me for the link.
To update the site if there is a new version of github cd to the ~/NLPP/NLPP directory (but not ~/NLPP/NLPP/NLPP) and then
1. `git pull`
	* If there is a merge conflict, then use `git reset --hard`, but be aware that this will overide all files on the site, so don't do this in production
	* To save the changes that are on the server, such as for the database use the following commands
		1. `git stash`
		2. `git pull`
		3. `git stash pop`
		4. `git checkout --theirs path/to/conflicted/file` <— (ie. NLPP/db.sqlite3)
		5. `git merge`

2. `touch /var/www/alearningcurve_pythonanywhere_com_wsgi.py`     
	* this command will restart the webserver so your changes appear, but it will take a few seconds, so be patient!
	
3. If the website is unavailible, the site's free trail may of expired and will need to be restarted by me (William Walling-Sotolongo) in order to be viewed

# Comment, Concerns, and Collaboration
If you have anything to say about the project leave a comment or email me at willwallsoto@gmail.com
