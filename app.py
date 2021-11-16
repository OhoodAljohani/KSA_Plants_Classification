from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf

from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

dic = {0 : 'CARYOPHYLLACEAE', 1 : 'BORAGINACEAE'}

model = load_model('./model/flora.h5')

model.make_predict_function()

def pred(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    img_array = image.img_to_array(img)

    img_batch = np.expand_dims(img_array, axis=0)

    img_preprocessed = preprocess_input(img_batch)

    
    prediction = model.predict(img_preprocessed)

    return prediction[0]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("main.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = pred(img_path)
		p = p.astype(int)

	return render_template("main.html", prediction = dic.get(np.asscalar(p)), img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
