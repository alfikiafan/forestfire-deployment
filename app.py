from flask import Flask, request, jsonify, Response
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

@app.route("/metadata")
def metadata():
    res = requests.get("http://localhost:8501/v1/models/forestfire-prediction")
    return res.json()

@app.route("/metrics")
def metrics():
    prometheus_url = "http://localhost:8501/monitoring/prometheus/metrics"
    response = requests.get(prometheus_url)
    return Response(response.text, content_type="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)