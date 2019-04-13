Commands
========
Lives in core app.

setup
*****
Calls:
codeblocks:: bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py generatekey
in order.

generatekey
***********
Creates a secret key and stores in .env file.

startapp(override)
******************
Starts app in app directory. Do not worry about the folder location