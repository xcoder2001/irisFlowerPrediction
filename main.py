# app/main.py

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/iris_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        inputs = [float(x) for x in request.form.values()]
        final_input = np.array(inputs).reshape(1, -1)
        prediction = model.predict(final_input)[0]

        labels = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        result = labels[prediction]

        return render_template("index.html", prediction_text=f"Predicted Species: {result}")
    except:
        return render_template("index.html", prediction_text="Please enter valid numeric values!")

if __name__ == "__main__":
    app.run(debug=True)
