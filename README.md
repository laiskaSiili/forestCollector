# forestCollector
A small django project to teach and learn. Allows to collect forest stand attributes and associated spatial information.

---

# Setup
0. Make sure python 3.7 or higher is installed and added to your path variable.
1. Clone or download repository to local machine.
2. In the terminal, move to the main folder called forestcollector which contains the __Pipfile__.
3. Use [pipenv](https://docs.pipenv.org/en/latest/) to replicate the python virtual environment with this command in terminal: __pipenv install --python 3.7__
4. If all went well, your virtual environment is ready. Activate it with this command in terminal: __pipenv shell__
5. Setup the database using the following command in terminal: __python manage.py migrate__
6. Create a superuser with this command in terminal: __python manage.py createsuperuser__
7. Spin up Django development server with this command in terminal: __python manage.py runserver__
8. Open localhost:8000/admin in your browser and login in as superuser. Create other users, either as collectors or not.
9. Go to localhost:8000 and login as the newly creater users.
