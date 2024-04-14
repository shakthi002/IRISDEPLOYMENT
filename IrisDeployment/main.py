from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Function to predict the iris class
def predict_iris_class(sepal_length, sepal_width, petal_length, petal_width):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    if prediction[0]=="virginica":
        return "ClassA"
    elif prediction[0]=="setosa":
        return "CLassB"
    else:
        return "ClassC"
    # return prediction[0]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        mapper = {0:'setosa', 1: 'versicolor', 2: 'virginica'}
        # Predict the iris class
        prediction = predict_iris_class(sepal_length, sepal_width, petal_length, petal_width)
        # prediction = mapper[prediction]
        return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
