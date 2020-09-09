# ::: Import modules and packages :::
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Import Keras dependencies
import keras
from tensorflow.python.framework import ops

ops.reset_default_graph()
from keras.preprocessing import image

# Import other dependecies
import numpy as np
import os

# ::: Flask App Engine :::
# Define a Flask app
app = Flask(__name__)
os.getcwd()

# print('Model loaded. Check http://127.0.0.1:5000/')
# model = keras.models.load_model('D:/Documents/sport/james_vs_nadal.h5')
model = keras.models.load_model("./models/james_vs_nadal_v2.h5")
# img_path = 'D:/Documents/deploy/uploads/james17.jpg'

# ::: MODEL FUNCTIONS :::
def model_predict(img_path, model):
    """
    Args:
            -- img_path : an URL path where a given image is stored.
            -- model : a given Keras CNN model.
    """

    IMG = image.load_img(img_path, target_size=(200, 200))
    IMG_ = np.expand_dims(image.img_to_array(IMG), axis=0)
    IMG_ /= 255.0
    prediction = model.predict(IMG_)[0][0] * 100

    return prediction


# ::: FLASK ROUTES
@app.route("/", methods=["GET"])
def index():
    # Main Page
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        # Get the file from post request
        f = request.files["file"]

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, "uploads", secure_filename(f.filename))
        f.save(file_path)

        # Make a prediction
        prediction = model_predict(file_path, model)

        return "{:f}".format(prediction)


# TODO: set server in dev mode
#
if __name__ == "__main__":
    # app.run()
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='0.0.0.0', port=8080)
