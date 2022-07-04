#!/bin/bash

cat myweb/settings.py | grep ALLOWED_HOST | grep \'*\' >> /dev/null
if [ $? -ne 0 ]; then
        echo "You have to set ALLOWED_HOST = ['*'] in ./myweb/settings.py"
        exit 1
fi

python manage.py runserver 0.0.0.0:5000
