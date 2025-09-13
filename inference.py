# inference.py
import joblib
import re

# Load saved artifacts
clf = joblib.load("random_forest_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

def predict_new_file(file_path):
    """Predict class for a single .bytes file"""
    with open(file_path, "r", errors="ignore") as f:
        content = f.read()
        content = re.sub(r'[^0-9A-Fa-f]', '', content)
    
    X = vectorizer.transform([content])
    pred = clf.predict(X)
    return le.inverse_transform(pred)[0]
