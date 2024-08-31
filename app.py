from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import os

app = Flask(__name__)

# Load the Keras model
model = load_model("mnist_model_ann.h5")

def predict_number(img_path):
    img = Image.open(img_path)
    img = img.resize((28, 28))
    img = img.convert('L')
    new_image=np.array(img)
    new_image[new_image==255]=0
    plt.imshow(new_image, cmap='gray')
    
    image=np.array(new_image).flatten()
    timg = image.reshape((1, 784))
    raw_predictions = model.predict(timg)
    predicted_class = np.argmax(raw_predictions, axis=-1)
    classname = str(predicted_class[0])
    confidence_score = np.max(raw_predictions)
    print("confidence_score of Class: ", classname)
    print("confidence_score ", confidence_score)
    return classname,confidence_score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    try:
        # Save the uploaded file temporarily
        upload_path = "temp_image.jpg"
        file.save(upload_path)

        # Perform prediction
        result = predict_number(upload_path)[0]
        
        #accuracy
        accuracy = predict_number(upload_path)[1] * 100
        confidence_score = "{:.2f}".format(accuracy)
        # Remove the temporary file
        os.remove(upload_path)

        return jsonify({"prediction": result,"accuracy":confidence_score})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
