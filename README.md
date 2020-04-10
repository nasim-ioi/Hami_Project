# Description
> this project is a RestApi system with CRUD opreation on the Blog model only by authenticated users
(who have signed up and logged in to the system by calling `http://127.0.0.1:8000/signup/` and `http://127.0.0.1:8000/login/`)
Also this project has document that includes UML Diagram and postman_export_apis json file which can be imported and run in
the postman for testing all urls and description of their opreations, with differrent methods, are included in this file.

## requirements:

  - python version : 3.7.5
  
  - Django : 2.2
  
  - djangorestframework : 3.9
  
  - djangorestframework-jwt : 1.11.0

## Setup
 
The first thing to do is cloning the repository:

```
git clone https://github.com/nasim-ioi/Hami_Project.git
cd Hami_Project
```

to install dependent packages and activate the virtual environment shell, run the below commands:

```
pipenv install
pipenv shell
```

to config and create tables in the database, run the below commands:

```
cd TestProject
python manage.py makemigrations
python manage.py migrate
```

to run the project's server use the following command:
```
python manage.py runserver
  
