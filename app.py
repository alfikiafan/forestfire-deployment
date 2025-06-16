from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MODEL_NAME = "forestfire-prediction"
TF_SERVING_URL = f"http://localhost:8501/v1/models/{MODEL_NAME}:predict"

@app.route("/")
def home():
    return "Forest Fire Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    response = requests.post(TF_SERVING_URL, json=data)
    return jsonify(response.json())