# Student Portal

A basic Django web app for managing student records. Includes user login/logout and CRUD operations for students with subject-wise marks.

## Setup

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
