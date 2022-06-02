FROM python:3.9.2

# The enviroment variable ensures that the python output is sent straight
# to the terminal with out buffering it first
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /URL_Shortner_Django_Service

ENV APPDIR=/URL_Shortner_Django_Service

# Set the working directory to /music_service
WORKDIR $APPDIR

# Copy the current directory contents into the container at /music_service
COPY . $APPDIR/


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


