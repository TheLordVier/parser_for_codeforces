# Parser for Codeforces

## Technology Stack

* Python 3.10
* Django
* Django REST framework
* PostgreSQL
* Docker and Docker Compose
* Celery
* Redis
* flake8
* Unittest


## Brief Description

This project is a parser designed to extract information about programming problems from codeforces.com and store it in 
a database. It's developed using Python 3.10 and Django REST framework. The project includes documentation generation 
via Redoc and employs Celery for asynchronous task execution. Redis is used as the message broker, and PostgreSQL serves
as the database. Notably, the project integrates with Telegram for the purpose of selecting problems based on their 
level of complexity and topic, and it can also construct contests consisting of 10 problems.


## Installation Guide

1. Create a .env file following the example in the .env.example file.

2. Install the project's dependencies listed in the requirements.txt file.

3. Launching containers with the command:

   ```bash
   docker-compose up -d
   ```

4. Create migrations:

   ```bash
    python manage.py makemigrations
   ```

5. Apply migrations:

   ```bash
    python manage.py migrate
   ```

6. Launch a Celery Worker to handle asynchronous tasks:

    ```bash
    celery -A parser_config worker -P eventlet -l INFO 
   ```
   
7. Launch a Celery Beat initializes Celery-beat, which is responsible for scheduling periodic tasks:

   ```bash
    celery -A parser_config beat -l info -S django 
   ```
   
8. Start the server:

   ```bash
   python manage.py runserver
   ```
   
9. To run the Telegram bot, execute the following command:

   ```bash
    python manage.py telegram_bot
   ```
