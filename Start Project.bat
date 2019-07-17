@echo off
cd /
REM This points to the correct directory for a local github install of the project.
cd C:\Users\Student3\Documents\GitHub\UTC-STUDENT-PROJECT\TeamX
python manage.py migrate
python manage.py makemigrations --merge
python manage.py migrate
python manage.py makemigrations 
python manage.py runserver
pause