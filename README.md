Django Local Library
---------------------------------------------------------------------------------------------------------------------------
For detailed information about this project go to this link: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website
--------------------------------------------------------------------------------------------------------------------------
Setting up a Django development environment
--------------------------------------------------------------------------------------------------------------------------------------

I did this using Windows. So here goes the setup for windows 10.

1. Check if you have python installed in your machine already :
command : python --version
if not download it from python's official site. Here's the link: https://www.python.org/downloads/
**make sure to check on the " Add Python ... to Path"**

2. Installing pip. If you installed python correctly it will be installed along side the python earlier. To check it existence type **pip --version** in cmd

3. Installing Django. For checking use the command: **django-admin --version**
Now, for installing django let's not disturb the entire system. Instead create a virtual environment and install django inside that environment. 

 a) Installing the virtual environment wrapper.  
 command: pip install virtualenvwrapper-win <br>
 b) Creating the environment.
 command: mkvirtualenv THENAMEYOUWANTTOGIVE
 
  N.B: for entering into the virtual environment anytime from cmd use the command :cd path_of_your_virtual_environment\Scripts\activate OR use the command: workon THENAMEYOUWANTTOGIVE
  
 c) installing django.
 command: pip install django
 for checking if it's installed or the version run **django-admin -version**
  N.B: Django is now installed in your virtual environment, not in your whole system.

Now, the virtual environment and django set up is done, and one is good to go! Cheers!

---------------------------------------------------------------------------------------------------------

Setting up the Project
------------------------------------------------------------------------------------------------------
After cloning run these command:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py migrate --run-syncdb

You will be asked to create a superuser by giving an email address, username and password. Do that.

**Command to run the server: python manage.py runserver

Now, you can use that superuser to login and create other user from the admin page. link: http://127.0.0.1:8000/admin/
The catalog page's link: http://127.0.0.1:8000/catalog/

--------------------------------------------------------------------------------------------------------------------------------
Commad for running the test files:
 1. python manage.py test
 2. python manage.py collectstatic