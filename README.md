# Description
this project is a RestApi system with CRUD opreation on the Blog model only by authenticated users
(who have signed up and logged in to the system by calling http://127.0.0.1:8000/signup/ and http://127.0.0.1:8000/login/)
Also this project has document that includes UML Diagram and postman_export_apis json file which can be imported and run in
the postman for testing all urls and description of their opreations, with differrent methods, are included in this file.


# Installation
 

## requirements:


  - python version : 3.7.5
  
  - Django : 2.2
  
  - djangorestframework : 3.9
  
  - djangorestframework-jwt : 1.11.0


After cloning the project you can run that on your local environment.To do this :

    1. run "pipenv install" to install required packeages and run "pipenv shell" to activate the virtual environment.
    
    2. move to this path Hami_Project/TestProject/ and run "python manage.py makemigrations" and "python manage.py migrate" 
       to create tables in the database.
    
    3. then run "python manage.py runserver" to run the server and call your desired api from Browser or Postman.
       Also you can create an admin to see the Django-Pannel by run "python manage.py createsuperuser" command.
  
