# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR .

# copy the dependencies file to the working directory
COPY deploy/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt --use-feature=2020-resolver

# copy the content of the local src directory to the working directory
COPY deploy/ .

# set the server in dev mode
# ENV  FLASK_ENV=development

# command to run on container start
EXPOSE 8080
# CMD [ "python", "./app.py" ]
CMD ["gunicorn"  , "--bind", "0.0.0.0:8080", "wsgi:app"]