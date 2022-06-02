## Clone Git Repository or Download Code ( inside folder where you want the code ) 
https://github.com/m55an5/URLShortner_django

## from the root folder

## docker build image
docker build -t django-url-shortner-app .

## run container 
docker container run -it -p 8000:8000 django-url-shortner-app 
