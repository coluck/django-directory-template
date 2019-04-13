Structure
---------
This project has the following directory structure::

    project_name/
    ├── app/
    │   ├── core/       # custom commands ex: py manage.py generatekey, setup
    │   └── users/      # overridden django user model
    │
    ├── config/         # includes a bunch of settings, url and wsgi
    │   ├── settings/
    │   │    ├── base,py             # inherited by development or production.py
    │   │    ├── development.py      # uses django debug toolbar
    │   │    ├── production.py       # production settings, debug = False
    │   │    ├── settings-default.py # default settings file created by django.admin
    │   │    ├── .env-example        # an example how should be the .env file
    │   │    └── .env                # in .gitignore, automatically will created
    │   │
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── locale/     # locale path for internationalization
    ├── static/     # static folder
    │   ├── css/
    │   ├── img/
    │   └── js/
    │
    ├── templates/  # templates folder
    └── manage.py
