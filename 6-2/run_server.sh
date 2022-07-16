#!/bin/bash

required_pkg='djangorestframework Pillow django-cors-headers'
pkg_list=($required_pkg)

for package in ${pkg_list[@]};
do
        if [ -z "$(pip list | grep -i ${package})" ]; then
                pip install ${package}
        else
                echo "${package} already installed"
        fi
done

cat myboard/settings.py | grep ALLOWED_HOST | grep \'*\' >> /dev/null
if [ $? -ne 0 ]; then
        echo "You have to set ALLOWED_HOST = ['*'] in ./myboard/settings.py"
        exit 1
fi

python manage.py runserver 0.0.0.0:5000
