**Create project**
   django-admin startproject bellepoule .

**Initialize sql DB**
   python manage.py migrate

**Super user**
   python manage.py createsuperuser

**SHELL**
   python manage.py shell



**Application (website)**
1. Create app
   python manage.py startapp website

2. Add models into sql db (2 steps)
   python manage.py makemigrations website
   python manage.py migrate        website



**Run**
   python manage.py runserver 0:8080
