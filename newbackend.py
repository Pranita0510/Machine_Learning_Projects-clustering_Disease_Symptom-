# backend.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

disease_data = pickle.load(open('Disease_Symptom.pkl', 'rb'))

def find_matching_cases(symptom_input):
    matches = disease_data.copy()
    for key, value in symptom_input.items():
        if key in matches.columns:
            matches = matches[matches[key] == value]
    return matches.head(5).to_dict(orient="records")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = find_matching_cases(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
