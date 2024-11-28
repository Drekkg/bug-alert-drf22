# Bug Alert Django Rest Framework Back End

## DRF Overview

Bug Alert DRF is the back end for the Bug Alert React Application.
It serves as a model of the database to store the information regarding
projects that wish to be tracked, issues, bugs and console errors that have observed. Bug Alert DRF conssits of three apps and models that store, update, retrieve and delete all neccassary information.

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

## Deployment

### Local Deployment

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file in the root directory and add the following:

   ```env
   SECRET_KEY=your-secret-key
   DATABASE_URL=your-database-url
   ```

5. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Deployment to Heroku

1. Create a new Heroku app:

   ```bash
   heroku create your-app-name
   ```

2. Set up environment variables on Heroku:

   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DATABASE_URL=your-database-url
   ```

3. Push the code to Heroku:

   ```bash
   git push heroku main
   ```

4. Apply migrations on Heroku:

   ```bash
   heroku run python manage.py migrate
   ```

5. Create a superuser on Heroku:
   ```bash
   heroku run python manage.py createsuperuser
   ```

## Credits

### Content

- [Source of content, if applicable]

### Media

- [Source of images, videos, or other media]

### Acknowledgements

- [Any acknowledgements or thanks]

## Acknowledgements

- [Thank anyone who helped or inspired you in the creation of this project.]
