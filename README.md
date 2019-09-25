# forestCollector
A small django project to teach and learn. Allows to collect forest stand attributes and associated spatial information.

---

# Setup
0. Make sure python 3.7 or higher is installed and added to your path variable.
1. Clone or download repository to local machine.
2. Install the packages listed in requirements.txt.
3. Setup the database using the following command in terminal: __python manage.py migrate__
4. Create a superuser with this command in terminal: __python manage.py createsuperuser__
5. Spin up Django development server with this command in terminal: __python manage.py runserver__
6. Open localhost:8000/admin in your browser and login in as superuser. Create other users, either as collectors or not.
7. Go to localhost:8000 and login as the newly creater users.
