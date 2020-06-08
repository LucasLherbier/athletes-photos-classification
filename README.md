# Athletes photos classification

This repository is an ongoing personal project combining my passion for sport with data science.

## Description of the project

### Goal

The goal of the project is to implement a *Python* servor, as an application, allowing to classify pictures between famous athletes. For the moment, the application is only for two sportmen, [Lebron James](https://en.wikipedia.org/wiki/LeBron_James) and [Rafael Nadal](https://en.wikipedia.org/wiki/Rafael_Nadal), but new ones will be added soon.


## Description of this repository

* the `CNN_sport.ipynb`: it explains how the deep learning model has been created
* **data**: access to the project resources such as the pritimive cell data <a href="#section1">*</a> studied here
* **deploy**: it contains the Flask application. It is divided in diverses part :
  * **static**: it containis a [*CSS*](https://www.w3schools.com/css/) file for styling the application and a [*JavaScript*](https://www.w3schools.com/js/) file that adds dynamic behavior to the page.
  * **templates**: it is composed of [*HTML*](https://www.w3schools.com/html/) scripts in which the variable data can be inserted dynamically. A template is rendered with specific data to produce a final document. The goal is to avoid generating HTML content from Python code is inconvenient
   Flask uses the Jinja template library to render templates.
  * **uploads**: sotrage folder for all the uploaded pictures
  * `app.py`: it explains how the deep learning model has been created



<small> * because of the size file, the **MLPOS-2.19000.zip** does not contain all the 19 000 configurations but only part </small>
 




