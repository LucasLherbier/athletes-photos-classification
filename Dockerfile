# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR .

# copy the dependencies file to the working directory
COPY deploy/requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt --use-feature=2020-resolver

# copy the content of the local src directory to the working directory
COPY deploy/ .

# Set the image environment
# ENV DOCKER_ENV=dev
# ENV DOCKER_ENV=prod

# RUN if [ "$DOCKER_ENV" = "prod" ] ; then echo Argument not provided ; else echo Argument is $arg ; fi

# command to run on container start
EXPOSE 8080
# CMD [ "python", "./app.py" ]
CMD ["gunicorn"  , "--bind", "0.0.0.0:8080", "wsgi:app"]