from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("forestfire-prediction")

app = Flask(__name__)

@app.route("/")
def home():
    return "Forest Fire Prediction Model is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = np.array(data["input"]).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({"prediction": prediction[0].tolist()})
