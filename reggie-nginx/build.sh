#!/bin/bash

# collects the webapp and django static files for nginx

cd ../reggie-app/
npm run build
cp -r build ../reggie-nginx	
cd ../reggie-nginx
mv build frontend

cd ../reggie-server
python manage.py collectstatic --noinput
