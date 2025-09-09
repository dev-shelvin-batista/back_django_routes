
# Project details
This project functions as a backend project developed in Django REST API, modularized and serialized with a PostgreSQL database.

| |Version |
|----------------|-------------------------------|
|Python |`11.5.2` |
|Django |`22.14.0`|
|PostgreSQL |`12`|

## Important note
- The postman_collections file has been added with all the developed REST APIs.

## Instructions
To start this project on a local server, follow the instructions below.

- Clone the project, either with the command git clone `https://github.com/dev-shelvin-batista/back_django_routes.git` or using a GitHub graphical tool.
- After cloning the repository, access the downloaded folder with the cd command in the terminal, i.e., `cd back_django_routes`, as several commands will be executed there.
- Activate the Python environment for the global constants that will be used in the project with the commands:  `python -m venv env` `source env/Scripts/activate`. It is recommended to run the last command in the git command terminal of the project folder.
- Install the necessary dependencies used for testing with the command: `pip install -r requirements.txt`
- Create the database in your preferred administrator. For example, you can use `pgAdmin `to create the database and `DBeaver` to connect to it and view the table structure. For testing purposes, the name **db_django_routes** was used, but you can use another name.
- Change the connection to the database file `back_django_routes/settings.py` in the project. In this file, modify the dictionary or the **DATABASES** object, which has the attributes for the default connection. Modify the *USER* and *PASSWORD* attributes, which are configured during the installation of **PostgreSQL** on your computer, and *NAME*, which corresponds to the name of the database you generated in the previous step.
- Run the migrations to generate the table structure in the created database. This is done with the command: `python manage.py migrate` or execute them one by one with the following commands `python manage.py migrate cities 0001` `python manage.py migrate users 0001` `python manage.py migrate stops 0001` `python manage.py migrate routes 0001`
- At this point, the project is ready to be tested. Run it with the command: `python manage.py runserver`. By default, the URL `http://localhost:8000/` is used to run the REST services.