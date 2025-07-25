import joblib
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import predict_clickbait
from urllib.parse import unquote

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'combined.joblib')

model_components = joblib.load(model_path)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing "title" field in request body'}), 400

    prediction_title = unquote(data['title'])

    return jsonify(predict_clickbait(prediction_title, model_components)), 200

@app.route('/health', methods=['GET'])
def health():
    try:
        if model_components:
            return jsonify({
                'status': 'healthy',
                'message': 'Clickbait API is running',
                'model_loaded': True
            }), 200
        else:
            return jsonify({
                'status': 'unhealthy',
                'message': 'Model not loaded',
                'model_loaded': False
            }), 503
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e),
            'model_loaded': False
        }), 500

@app.route('/')
def index():
    return jsonify({'message': 'Clickbait Prediction API'}), 200

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, host='localhost', port=8000)