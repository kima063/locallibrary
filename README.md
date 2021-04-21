# locallibrary
Setting up a Django development environment
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
 
  N.B: for entering into the virtual environment anytime from cmd use the command : path_of_your_virtual_environment\Scripts\activate OR use the command: workon THENAMEYOUWANTTOGIVE
  
 c) installing django.
 command: pip install django
 for checking if it's installed or the version run **django-admin -version**
  N.B: Django is now installed in your virtual environment, not in your whole system.

Now, the virtual environment and django set up is done, and one is good to go! Cheers!
