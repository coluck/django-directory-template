Quickstart
==========
.. code-block:: bash

    # Create a root directory
    $ mkdir project && cd project/

    # Make sure we have an up-to-date version of django 2.2
    $ django-admin startproject --template=blabla.zip [project_name]

    # Install dependencies django-debug-toolbar, python-decouple
    $ pip3 install -r requirements.txt

    # One shot makemigrations and migrate
    $ python manage.py setup

    # Overriden startapp command creates app in app directory
    # Do not worry about the folder location
    $ python manage.py startapp blog

    # Generate secret key in .env file
    $ python manage.py generatekey

