To setup locally:

Make sure virtualenv is setup properly:
Add to your ~/.bashrc or ~/.zshrc (depending which you're using) the following anywhere:
source /usr/local/bin/virtualenvwrapper.sh

1. mkvirtualenv rs
2. vim ~/.virtualenvs/rs/bin/activate
3. append these to the end of that file:
export DJANGO_SETTINGS_MODULE="settings.jordan"
export SECRET_KEY_LOCAL=420v-23dl-avie-3
(Replace 'jordan' with the name of your settings file, ex. james or whichever you want to use in /project/settings/)
4. workon rs (this activates that the newly created virtualenv that is pointing to this project's settings file)
5. from the project root run: pip install -r requirements.txt (any python modules required for this project are entered there)
6. create your db
   if postgres: sudo su postgres; psql; create database restaurant; (control d to quit)
   if mysql: >mysql; create database restaurant;
7. run ./manage.py migrate
8. run ./manage.py createsuperuser
9. run ./manage.py runserver 127.0.0.1:8001 (http://127.0.0.1:8001/admin/ should show login screen)