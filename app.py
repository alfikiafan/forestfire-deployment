from flask import Flask, request, jsonify
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

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

@app.route("/metadata")
def metadata():
    res = requests.get(f"http://localhost:8501/v1/models/{MODEL_NAME}")
    return res.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)