import os
import sys
import joblib
import warnings
warnings.filterwarnings("ignore")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

from backend.api.utils import predict_clickbait


# Model loading test
try:
    MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'backend', 'models', 'combined.joblib')
    model_components = joblib.load(os.path.abspath(MODEL_PATH))
    print("[SUCCESS] Model loaded successfully")
except FileNotFoundError:
    print(f"[ERROR] Model file not found: {MODEL_PATH}")

# Test the predict_clickbait function
try:
    test_titles = [
        "Google Cloud Associate Cloud Engineer Course - Pass the Exam!",
        "Scientists discover new method for treating cancer",
        "You Won't Believe What Happened Next!"
    ]

    # print("Clickbait Prediction Tests:\n")

    for title in test_titles:
        result = predict_clickbait(title, model_components)
        # print(f"Title: {title}")
        # print(f" → NB Probability:       {result['nb_probability']:.3f}")
        # print(f" → RF Probability:       {result['rf_probability']:.3f}")
        # print(f" → Combined Probability: {result['combined_probability']:.3f}")
        # print(f" → Prediction:           {result['prediction']}\n")

    # print("-" * 50)
    print("[SUCCESS] Clickbait prediction tests completed successfully")    
except Exception as e:
    print(f"[ERROR] Error during clickbait prediction tests: {e}")

