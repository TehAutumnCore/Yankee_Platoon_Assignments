# Intro to Django
https://github.com/Code-Platoon-Curriculum/curriculum/blob/main/07-Django/1-intro-to-django-orm/1-intro-django-orm.md 

## Creating Virtual Environment
-create a root directory called envs to store environments
-python -m venv <envname> | to create an environment
-Start the environment with | source <envname>/bin/activate
- to deactivate the env use | "deactivate"

## Installing pip and django
-pip install
-pip install --upgrade pip
-pip install django
django-admin | shows a list of available django commands |startapp & startproject

## Starting the project and creating the application
python -m django startproject pokedex_proj .     | creates a nested folder with 
# https://docs.djangoproject.com/en/5.1/ref/django-admin/
  python manage.py startapp pokemon_app    | will create the app

## Linking the application
# add the app under installed apps in the settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pokemon_app/'
]

# record all dependencies by creating the requirements.txt using the command
pip freeze > requirements.txt


# SQL
createdb pokedex_db
go to settings.py under DATABAES = {} 
and edit the engine to say postgresql instead of sqlite and change the name
to the name of the pokedex

# PSYCHOPG
https://www.psycopg.org/psycopg3/docs/basic/install.html
python -m pip install --upgrade pip 
pip install "psycopg[binary]"
make sure requirements is updated

# MODELS
https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-types/ 
django-admin
python manage.py makemigrations
makes a migrations folder with an init file and 0001_initial.py
in pokedex_db if you \d you can see if the information was passed if not: 
python manage.py migrate will send a list of applying migrations to the db
<!-- if db gets dropped, the migrate folder keeps a log and you can just migrate again -->
any changes that occur in models, need to be migrated
python manage.py makemigrations
python manage migrate

# Shell
python manage.py shell

from pokemon_app.models import Pokemon
pikachu = Pokemon('Pikachu',level=6)
pikachu
<Pokemon: Pokemon object(None)>
pikachu.save()
select * from pokemon_app.pokemon

from pokemon_app.models import Pokemon
pikachu2 = Pokemon('Pikachu',level=12)
pikachu2
pikachu.save()
<!-- Will give an error since Pokemon('Pikachu',) already exists -->

charizard = Pokemon('Charizard',level=32, captured=True,description='A big orange dragon with a bad temper')
charizard.save()
Pokemon.objects.all()
all_pokemon[0]
all_pokemon[0].name

charizard = Pokemon.objects.all()[1]
p1 = Pokemon.objects.all().filter(level=1)
p1
<QuerySet [<Pokemon: Pikachu Has not been captired>]>
p2 = Pokemon(name='Totodile',level=9,captured=True)

# Fixtures
-Create a fixtures folder in pokemon_app |     mkdir pokemon_app/fixtures
python manage.py dumpdata pokemon_app.model
python manage.py dumpdata pokemon_app.Pokemon --indent 2 > pokemon_app/fixtures/pokemon_data.json | generates a dumpdata json file


# 
python manage.py loaddata pokemon_data.json
update admin.py