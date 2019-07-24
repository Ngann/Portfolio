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




error:
pip3 install pillow
pip3 install psycopg2
pip3 install psycopg2-binary