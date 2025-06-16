from flask import Flask, request, jsonify
import numpy as np
from keras.layers import TFSMLayer
from keras import Model, Input

layer = TFSMLayer("forestfire-prediction", call_endpoint="serving_default")

input_tensor = Input(shape=(12,))
model = Model(inputs=input_tensor, outputs=layer(input_tensor))

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
