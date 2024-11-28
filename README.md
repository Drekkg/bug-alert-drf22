# Bug Alert Django Rest Framework Back End

## Overview

Bug Alert DRF is the back end for the Bug Alert React Application.
It serves as a model of the database to store the information regarding
projects that wish to be tracked, issues, bugs and console errors that have observed. Bug Alert DRF conssits of three apps and models that store, update, retrieve and delete all neccassary information.

**Live Site**

https://bug-alert-drf-7540ff833a9e.herokuapp.com/

**Repository**

https://github.com/Drekkg/bug-alert-drf22.git

**Author**

Derek Garnett

## User Experience (UX)

Working correctly the user should not be aware of Bug Alert DRF.
The data is seamlessly manipulated in the background.

## Features

Full CRUD functionality.
Create - The user can create a project and add issues and comments.
Retrieve - The user can read the data for projects, issues and comments.
Update - The user can make changes to the project.
Delete - The user can delete a project and all relavant issues and comments.

### Features Left to Implement

- Updating issues and comments
- Deleting individual comments and issues

## Technologies Used

- Django rest framework 3.4
- Django allauth 0.50
- Django dj-rest-auth 2.14
- Django simplejwt 4.7

### Languages

Python 3

## Testing

**Manual Testing**

- The deployed Bug Alert DRF was extensively tested through the front end.
  Projects, issues, comments, and resolved status were properly retrieved, updated and deleted.
  Furthermore accessing the database on Heroku the correct behaviour could be observed.
  The following screenshots confirm observed behaviour.

  **Adding a project**

  A project named "Test Test Test" is added to the table.

![add project](bug_alert_drf/assets/add_project.png)

An issue named "Test 1" and "Test 2" are added to the issues table.

![add isssue](bug_alert_drf/assets/test_issue.png)

Comments "Test issue 1 comment" and "Test issue 2 comment" are added to the comments table.

![add comments](bug_alert_drf/assets/test_comment.png)

The project "Test Test Test" is deleted and as expected the related comments and issues are also deleted.

![delete project](bug_alert_drf/assets/delet_project.png)

![delete Issue](bug_alert_drf/assets/delete_issue.png)

![delet comment](bug_alert_drf/assets/delete_comment.png)

## Database

The DB is is a postgres relational database and consists of three apps and models.

**User**

Created automatically by Django Restframework

**Projects**
Contains the following fields:

id (PK)

name

description

owner_id (FK to User)

created_at

updated_at

**Issues**
Contains the following fields:

id (PK)

title

description

project_id (FK to Project)

owner_id (FK to User)

created_at

updated_at

resolved

**Comments**
id (PK)

text

issue_id (FK to Issue)

owner_id (FK to User)

created_at

updated_at

**Entity Relationship diagram**

![erd_diagram](bug_alert_drf/assets/entity_diagram.png)

All models contain an appropriate serializer to convert the querysets into JSON and vice versa.
All models have appropriate views and URL patterns to direct the data to the correct table.

## Issue and Bugs

The database works without any major errors.
The design of the models though functional could be improved.
A get request to the issues and comments will retrieve all comments and issues
which is then filtered on the front end. This should be filterd on the back end and is slated as feature to be added in a future release.

## Python Validation

###Projects

**models.py**

![models](bug_alert_drf/assets/project_models.png)

**serializers.py**

![serializer](bug_alert_drf/assets/project_serializer.png)

**urls.py**

![urls](bug_alert_drf/assets/urls_projects.png)

**views.py**

![views](bug_alert_drf/assets/views_project.png)

## Issues

**models.py**

![models issues](bug_alert_drf/assets/issues_models.png)

**serializers.py**

![serializer issue](bug_alert_drf/assets/serializers_issue.png)

**urls.py**

![urls issue](bug_alert_drf/assets/urls_issue.png)

**views**

![issue views](bug_alert_drf/assets/views_issues.png)

## Comments/Issue details

**models.py**

![comments model](bug_alert_drf/assets/comments_model.png)

**serializers.py**

![comments serializer](bug_alert_drf/assets/comment_serializer.png)

**urls.py**

![comments urls](bug_alert_drf/assets/comment_urls.png)

**views.py**

![comments views](bug_alert_drf/assets/comments_views.png)

**settings.py**
![settings py](bug_alert_drf/assets/settings.png)

Python files pass through the CI linter with no errors

## Deployment

### Deployment to Heroku

**Prepare the API for deployment**

- Step one you need to create a new Postgre Database.
- Full instructions are available in The Code Institute LMS.
- Log into Heroku and create a new App.
- Click on the settings Tab.
- Click on Reveal Config Vars
- In the Key field enter: DATABASE_URL
- In the value field paste in the url for your Database.
- It should look something like this: postgres://ub6ycb3fdvr:....................
- Back in the DRF app, in the terminal install the following packages:
  pip3 install dj_database_url==0.5.0 psycopg2
- In your settings.py file, import dj_database_url underneath the import for os:
  import os
  import dj_database_url

- update the DataBASES section:

if 'DEV' in os.environ:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}
else:
DATABASES = {
'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}

- Make sure to apply migrations to your database:

python manage.py makemigrations

python manage.py migrate

- install gunicorn.

pip3 install gunicorn django-cors-headers

- Freeze requirements

pip freeze --local > requirements.txt

- Create a procfile

- Inside the procfile add:

release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi

- In settings.py update the Allowed hosts to include the heroku app:

ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']

- Add corsheaders to INSTALLED_APPS
  INSTALLED_APPS = [
  ...
  'dj_rest_auth.registration',
  'corsheaders',
  ...
  ]

- Add cors headers to the top of Middleware:

SITE_ID = 1
MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
...
]

- Enable sending cookies:

CORS_ALLOW_CREDENTIALS = True

- Set JWT Samesite to None:

JWT_AUTH_SAMESITE = 'None'

- Put your secret Key in the env py and access it from settings:
  SECRET_KEY = os.getenv('SECRET_KEY')

- Create a new secret key in env.py:
  os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")

- Freeze requirements again:
  pip freeze --local > requirements.txt

- Back in Heroku, set a secret key:
  SECRET_KEY: "create a random string"

- Open the deploy tab and deploy!!

### Acknowledgements

- The Bug Alert DRF is based off the DRF walkthrough, and was adapted
  for its current use.

## Acknowledgements

- Thanks to my Mentor Juliia Konovalova
- My Partner Christine Steinbach
- Google
- Stack Overflow
- Django documentation
- GitHub Copilot was mainly for commits and code explanation.
