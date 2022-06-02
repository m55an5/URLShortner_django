## Clone Git Repository or Download Code ( inside folder where you want the code ) 
https://github.com/m55an5/URLShortner_django

## from the root folder

## docker build image
docker build -t django-url-shortner-app .

## run container 
docker container run -it -p 8000:8000 django-url-shortner-app 

## Test Cases
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/create-short-url/ -d "{\"original_url\":\"https://twitter.com/682632716\"}"

curl -X GET http://127.0.0.1:8000/api/FzyOFx
