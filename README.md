<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>MNIST Number Prediction with ANN</h1>
    <p>This project is a web application that allows users to upload images of handwritten digits and receive predictions using an artificial neural network (ANN). The model is built using Keras and Flask.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2 id="features">Features</h2>
    <ul>
        <li>Upload images in PNG, JPG, or JPEG formats.</li>
        <li>Receive predictions for handwritten digits.</li>
        <li>Display the confidence score of the predictions.</li>
        <li>Responsive design with Tailwind CSS for a better user experience.</li>
    </ul>

    <h2 id="installation">Installation</h2>
    <p>To set up the project locally, follow these steps:</p>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/wissalcharraki/mnist-digit-prediction.git</code></pre>

        <li>Navigate to the project directory:</li>
        <pre><code>cd mnist-digit-prediction</code></pre>

        <li>Create a virtual environment:</li>
        <pre><code>python -m venv venv</code></pre>

        <li>Activate the virtual environment:</li>
        <pre><code>source venv/bin/activate</code></pre>
        <p>(On Windows use: <code>venv\Scripts\activate</code>)</p>

        <li>Install the required packages:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

    <h2 id="usage">Usage</h2>
    <p>To run the application:</p>
    <ol>
        <li>Start the Flask server:</li>
        <pre><code>python app.py</code></pre>
        <li>Open your web browser and go to:</li>
        <pre><code>http://127.0.0.1:5000/</code></pre>
        <li>Upload an image of a handwritten digit and click on the "Predict Number" button to see the prediction.</li>
    </ol>

    <h2 id="contributing">Contributing</h2>
    <p>Contributions are welcome! Please follow these steps:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch for your feature or bug fix:</li>
        <pre><code>git checkout -b feature-branch</code></pre>
        <li>Make your changes and commit them:</li>
        <pre><code>git commit -m "Description of changes"</code></pre>
        <li>Push to the branch:</li>
        <pre><code>git push origin feature-branch</code></pre>
        <li>Open a pull request.</li>
    </ol>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

    <footer>
        <p>Created with &hearts; by [Your Name]</p>
    </footer>
</body>
</html>
