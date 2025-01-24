from flask import Flask, request, jsonify
import pickle
import numpy as np

cv = pickle.load(open("transform.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb")) 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Language Detector API!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "texts" not in data:
            return jsonify({"error": "Please provide a 'texts' field in your request."}), 400
        texts = data["texts"]

        if not isinstance(texts, list):
            return jsonify({"error": "The 'texts' field should be a list of strings."}), 400

        vectorized_texts = cv.transform(texts)
        y = model.predict(vectorized_texts)
        le = pickle.load(open("label_encoder.pkl", "rb")) 
        predictions = le.inverse_transform(y)

        return jsonify({"predictions": predictions.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
