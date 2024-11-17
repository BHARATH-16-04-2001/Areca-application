from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf # type: ignore
import tensorflow as tf # type: ignore

from tensorflow.compat.v1 import ConfigProto # type: ignore
from tensorflow.compat.v1 import InteractiveSession # type: ignore

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.2
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
# Keras
from tensorflow.keras.applications.resnet50 import preprocess_input # type: ignore
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='./areca.h5'

# Load your trained model
model = load_model(MODEL_PATH)


def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
   # x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    
    
    if preds==0:
        preds="Bud Borer Disease"
    elif preds==1:
        preds="healthy foot"
    elif preds==2:
        preds="Healthy Leaf"
    elif preds==3:
        preds="Healthy Nut"
    elif preds==4:
        preds="Healthy Trunk"

    elif preds==5:
        preds="Mahali Koleroga Disease"
    elif preds==6:
        preds="Stem Cracking Disease"
    elif preds==7:
        preds="Stem Bleeding Disease"
    elif preds==8:
        preds="Yellow Leaf Disease"
        
    
    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('home.html')


@app.route('/about.html', methods=['GET'])
def about():
    # Main page
    return render_template('about.html')
	
	
	
@app.route('/home.html', methods=['GET'])
def home():
    # Main page
    return render_template('home.html')
	

@app.route('/logout.html', methods=['GET'])
def logout():
    # Main page
    return render_template('login.html',msg="logout")
	


@app.route('/login.html', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username=request.form['username']
		password=request.form['password']
		
		if username=="Bharath" and password=="Areca":
			return render_template('index.html')
		else:
			return render_template('login.html',msg="failed")
		
	else:
		return render_template('login.html')
		
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

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        print(f"Result of prediction is : {result}")
        return result
    return None
    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
