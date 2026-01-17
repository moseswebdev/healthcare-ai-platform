# ai-service/app.py (FastAPI)
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load('./models/symptom_predictor.joblib')

class SymptomRequest(BaseModel):
    symptoms: str

@app.post("/predict")
async def predict(request: SymptomRequest):
    # Simple symptom vectorization
    symptom_vector = vectorize_symptoms(request.symptoms)
    prediction = model.predict([symptom_vector])
    confidence = model.predict_proba([symptom_vector]).max()
    
    return {
        "condition": prediction[0],
        "confidence": float(confidence),
        "recommendation": "Consult a healthcare provider"
    }

def vectorize_symptoms(text: str):
    # Simple demonstration - real implementation would use NLP
    keywords = {
        'fever': 1, 'cough': 2, 'headache': 3, 'fatigue': 4
    }
    vector = [0] * 10
    for word, idx in keywords.items():
        if word in text.lower():
            vector[idx] = 1
    return vector

# Health check for Kubernetes
@app.get("/health")
def health_check():
    return {"status": "healthy"}