pip3 install --upgrade pip
pip3 install --upgrade django
python -V

create project:
django-admin startproject portfolio

create app: app name should be plural
django-admin startapp jobs
- go to settings.py to add jobs app

run server:
python3 manage.py runserver

Url Paths:
urls.py 
- add path to jobs app and create a template and jobs folder with the home.html "hello world" setup

Database: Postgres.app // this allows for DB management 
- install Postgres.app , server setting make sure 
- intialize to start postgres server and will open a terminal
- double click on  postgres to open a new terminal

Setting up Db password:
postgres=# \password
Enter new password: 
Enter it again: 
postgres=# CREATE DATABASE portfoliodb;
CREATE DATABASE

Database migration:
- Update models.py and run migration
 python3 manage.py makemigrations 
Migrations for 'jobs':
  jobs/migrations/0001_initial.py
    - Create model Job

Database migrate:
python3 manage.py migrate
- ready to save information to database from Django

Database: Django Admin
- localhost:8000/admin/
- allows us to work with database via local host
- needs a user and password:
    - :portfolio-project $ python3 manage.py createsuperuser
    - Username (leave blank to use 'cereal'): ngan
    - Email address:                
    - Password: 
    - Password (again): 
    - Superuser created successfully.
- Now you should be able to log into the admin portal using the credential. 

Static files: run to find any new static files add it to a static folder at the top level.
- all static file in all apps, must be combines to on static folder
python3 manage.py collectstatic


error:
pip3 install pillow
pip3 install psycopg2
pip3 install psycopg2-binary