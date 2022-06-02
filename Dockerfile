FROM python:3.9.2-slim

# The enviroment variable ensures that the python output is sent straight
# to the terminal with out buffering it first
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /URL_Shortner_Django_Service

ENV APPDIR=/URL_Shortner_Django_Service

# Set the working directory to /URL_Shortner_Django_Service
WORKDIR $APPDIR

# Copy the current directory contents into the container at /URL_Shortner_Django_Service
COPY . $APPDIR/

# setup python virtual enviornment
RUN python -m venv drf_env
RUN /bin/bash -c 'source drf_env/bin/activate'

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run unit tests 
RUN python -m pytest urlshortner/ --cache-clear -v

# Setup DB and Migrations 
RUN python urlshortner/manage.py makemigrations
RUN python urlshortner/manage.py migrate

EXPOSE 8000

CMD python urlshortner/manage.py runserver 0.0.0.0:8000
