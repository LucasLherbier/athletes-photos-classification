# Athletes photos classification

This repository is an ongoing personal project combining my passion for sport with data science.

## Description of the project

### Goal

The goal of the project is to implement a *Python* server, as an application, allowing to classify pictures between famous athletes. The classification is based on an deep learning model using convolutional neural networks.  
For the moment, the application is only for two sportsmen, [Lebron James](https://en.wikipedia.org/wiki/LeBron_James) and [Rafael Nadal](https://en.wikipedia.org/wiki/Rafael_Nadal), but new ones will be added. 

### Description of this repository

* the `CNN_sport.ipynb`: it explains how the deep learning model has been created
*  **data**: it contains 30 examples of the athletes pictures
*  **dataset_from_google**: it contains the files to create a pictures dataset automatically from Google Images. You will find all the process [here](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/).
* **deploy**: it creates the *Flask* application. It is divided in diverse parts :
  * **static**: it contains a [*CSS*](https://www.w3schools.com/css/) file for styling the application and a [*JavaScript*](https://www.w3schools.com/js/) file that adds dynamic behavior to the page.
  * **templates**: it is composed of [*HTML*](https://www.w3schools.com/html/) scripts in which the variable data can be inserted dynamically. A template is rendered with specific data to produce a final document. The goal is to avoid generating HTML content from Python code is inconvenient.
  * **uploads**: storage folder for all the uploaded pictures
  * `app.py`: the *Flask* application - it imports the *Flask* module, creates a web server and instances of the *Flask* class -
 
 
 ### Organization
 * the pictures dataset has been automatically extracted using Google Images. The needed files are available in the folder **dataset_from_google**. A *JavaScript* script gathers image URLs which can be downloaded using a *Python* code. You will find all the process [here](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/).
 * the classificer model has been developed in the `CNN_sport.ipynb` with the [*Keras*](https://keras.io) library
 * the web server has been developed with the micro web framework [*Flask*](https://flask.palletsprojects.com/en/1.1.x/)
 
 
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

