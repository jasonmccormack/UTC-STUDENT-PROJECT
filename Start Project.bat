@echo off
cd /
REM This points to the correct directory for a local github install of the project.
cd C:\Users\Student3\Documents\GitHub\UTC-STUDENT-PROJECT\TeamX
python manage.py runserver 0.0.0.0:8000
pause