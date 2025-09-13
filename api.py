from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import joblib
import re

app = FastAPI(title="MalXGuard API")

# Allow requests from Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Load model artifacts
clf = joblib.load("random_forest_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    content = content.decode(errors="ignore")
    content = re.sub(r'[^0-9A-Fa-f]', '', content)
    X = vectorizer.transform([content])
    pred = clf.predict(X)
    return {"prediction": int(le.inverse_transform(pred)[0])}
