# -*- coding: utf-8 -*-
# autopep8 -i app.py
"""
Created on Thu Jun 5 11:39:57 2020
@author: Lucas Lherbier
"""

# --------------------------------- IMPORTS ---------------------------------
import os
import numpy as np
from keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from tensorflow import keras
from tensorflow.python.framework import ops
ops.reset_default_graph()


# Define a Flask app
app = Flask(__name__)
os.getcwd()

model = keras.models.load_model('./models/james_vs_nadal_v2.h5')


# -------------------------------- FUNCTIONS --------------------------------
def model_predict(img_path, model):
    ''' Apply the deep learning model to the image uploaded
    img_path: URL path where a given image is stored
    model: the Keras CNN model '''

    IMG = image.load_img(img_path, target_size=(200, 200))
    IMG_ = np.expand_dims(image.img_to_array(IMG), axis=0)
    IMG_ /= 255.
    prediction = model.predict(IMG_)[0][0]*100

    return prediction


# ::: FLASK ROUTES
@app.route('/', methods=['GET'])
def index():
    # Main Page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make a prediction
        prediction = np.round(model_predict(file_path, model), 2)
    if prediction > 50:
        return f"{prediction}% Nadal"
    else:
        return f"{(100-prediction)}% James"



# --------------------------------- MAIN ---------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)