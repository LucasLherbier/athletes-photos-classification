# Athletes photos classification

This repository is an ongoing personal project combining my passion for sport with data science.

A live version of the app can be found at https://stormy-savannah-71478.herokuapp.com

# Table of contents

* <a href='#Description of the project'> Description of the project</a>

[Description of the project](#Description of the project) 
   * [Goal](#Goal)
   * [Description of this repository](#"Description of this repository") 
   * [Organization](#Organization) 
* [Development Workflow](#Development Workflow) 
   * [Overall description](#Overall description) 
   * [Build the Docker image ](#Build the Docker image ) 
   * [Run server locally](#Run server locally) 
   * [Download the Docker image](#Download the Docker image) 
   * [Communications inside the container](#Communications inside the container) 
* [Extract of the application ](#Extract of the application ) 

## Description of the project

### Goal

The goal of the project is to implement a *Python* server, as an application, allowing to classify pictures between famous athletes. The classification is based on an deep learning model using convolutional neural networks.  
For the moment, the application is only for two sportsmen, [Lebron James](https://en.wikipedia.org/wiki/LeBron_James) and [Rafael Nadal](https://en.wikipedia.org/wiki/Rafael_Nadal), but new ones will be added. 

### Description of this repository

* `CNN_sport.ipynb`: it explains how the deep learning model has been created. It needs around 30s to load.
* `Dockerfile`: create a docker image for running the app as a container
* `heroku.yml`: create the heroku app. The Docker image will be built by heroku.
* **.github/workflows**: build the Docker image and push it on Docker Hub in the repo `glauda/athletes_classification`. 
*  **data**: it contains 30 examples of the athletes pictures
*  **dataset_from_google**: it contains the files to create a pictures dataset automatically from Google Images. You will find all the process [here](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/).
* **deploy**: it creates the *Flask* application. It is divided in diverse parts :
  * **static**: it contains a [*CSS*](https://www.w3schools.com/css/) file for styling the application and a [*JavaScript*](https://www.w3schools.com/js/) file that adds dynamic behavior to the page.
  * **templates**: it is composed of [*HTML*](https://www.w3schools.com/html/) scripts in which the variable data can be inserted dynamically. A template is rendered with specific data to produce a final document. The goal is to avoid generating HTML content from Python code is inconvenient.
  * **uploads**: storage folder for all the uploaded pictures
  * `app.py`: the *Flask* application - it imports the *Flask* module, creates a web server and instances of the *Flask* class -
  * `requirements.txt`: list of all packages needed to create the Docker image.
  * `wsgi.py`: WSGI (Web Server Gateway Interface) used to interface Flask server with web server in production mode.
 
 
 ### Organization
 * the pictures dataset has been automatically extracted using Google Images. The needed files are available in the folder **dataset_from_google**. A *JavaScript* script gathers image URLs which can be downloaded using a *Python* code. You will find all the process [here](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/).
 * the classifier model has been developed in the `CNN_sport.ipynb` with the [*Keras*](https://keras.io) library
 * the web server has been developed with the micro web framework [*Flask*](https://flask.palletsprojects.com/en/1.1.x/)
 
 
### Development workflow

#### Overall description
A Github workflow is used to build the [*Docker*](https://www.docker.com/) image and release it on [*Docker Hub*](https://hub.docker.com/). It allows building and sharing the image. Building the image on our personal laptops (with Windows) was too time consuming, especially due to the presence of library [*TensorFlow*](https://www.tensorflow.org/?hl=fr). 

The deployment in production is handled by [*Heroku*](https://www.heroku.com/). An automatic pipeline is used to build the Heroku app directly from the Github repository.

All the workflow can be summarised by the following diagram.

<figure>
  <img src="./data/worflow_dev.JPG" alt="Trulli" style="width:100%">
  <figcaption> <small><small> <i> Figure 4: Development Workflow.</i> </small> </figcaption>
</figure>

#### Build the Docker image 
Add a tag *build* to your commit, then push it on Github.
```
git add <updated-files>
git commit -m "<my-commit-message>"
git tag -a build "<build message>"
git push
```
The image will be build by the Github CI, and then published at https://hub.docker.com/repository/docker/glauda/athletes_classification

#### Run server locally
Download the Docker image
`docker pull glauda/athletes_classification:latest`

Create and run the container. If you want to modify the server and see the changes, go to the project main directory and bind the *deploy* folder to the container when running it.

Some changes might not appear because they are cached by your browser. For example, with Google Chrome, you can press `Crtl+Cap+r` to "force refresh" the page.
```
docker run -p 8080:8080 -it -v "$(pwd)"/deploy:/deploy glauda/athletes_classification python3 /deploy/app.py
```

Otherwise, you can open a shell the container and start the server
```
docker run -p 8080:8080 -it -v "$(pwd)"/deploy:/deploy glauda/athletes_classification /bin/bash
python3 app.py
```

Go to your browser, the server will be available at http://localhost:8080/


 ### Communications inside the container
Flask is not optimized to be used directly as a web server in production moode : you will find more details [here](https://flask.palletsprojects.com/en/1.1.x/deploying/). This is why a `wgsi` server is used to interface with the Flask server. The wsgi server is run using the *gunicorn* command. 

<figure>
  <img src="./data/communications_inside_container.JPG" alt="Trulli" style="width:100%">
  <figcaption> <small><small> <i> Figure 5: Communications inside the container.</i> </small> </figcaption>
</figure>

### Extract of the application

<figure>
  <img src="https://raw.githubusercontent.com/LucasLherbier/athletes-photos-classification/master/data/App_1.png" alt="Trulli" style="width:100%">
  <figcaption> <small> <i> Figure 1: Python server interface.</i>  </small> </figcaption>
</figure>
<br>

<figure>
  <img src="https://raw.githubusercontent.com/LucasLherbier/athletes-photos-classification/master/data/App_3.PNG" alt="Trulli" style="width:100%">
  <figcaption> <small> <i> Figure 2: Prediction for a Nadal picture. </i>  </small> </figcaption>
</figure>

<br>

<figure>
  <img src="https://raw.githubusercontent.com/LucasLherbier/athletes-photos-classification/master/data/App_2.PNG" alt="Trulli" style="width:100%">
  <figcaption> <small><small> <i> Figure 3: Prediction for a James picture.</i> </small> </figcaption>
</figure>

