from flask import Flask, request, jsonify,render_template
from flask.logging import create_logger
import logging


import numpy as np
import joblib
import os
import requests
from io import BytesIO
from sklearn.preprocessing import StandardScaler
from skimage.feature import hog
from PIL import Image, ImageFilter,ImageOps
from sklearn import svm

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/imageurl/<path:imgpath>")
def predict(imgpath):
    
    LOG.info(f"URL requested: {imgpath}")
    
    response = requests.get(imgpath)
    image = Image.open(BytesIO(response.content))
    #path = imgpath
    #image = Image.open(path)
    image = ImageOps.grayscale(image)
    image = ImageOps.equalize(image)
    image = np.asarray(image.resize([64,64]),dtype="int32")
    
    fd,hog_image = hog(image, orientations=8, pixels_per_cell=(16,16),
                   cells_per_block=(4, 4),block_norm= 'L2',visualize=True)
    
    hog_img = np.array(fd).reshape(1,-1)
    
    sc = joblib.load("std_scaler.bin")
    scaled_img = sc.transform(hog_img)
    
    predict = list(clf.predict(scaled_img))
    LOG.info(f"Logo Predicted as: {predict}")
    return jsonify({"Logo":predict})
    #return path 
    
    
if __name__ == "__main__":
    clf = joblib.load("logo_classifier.joblib")
    app.run(host='0.0.0.0', port=8088, debug=True)
    