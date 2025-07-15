from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")  # Assumes model was trained & saved

@app.get("/")
def root():
    return {"message": "Model is live!"}

@app.post("/predict")
def predict(features: list[float]):
    prediction = model.predict([features])
    return {"prediction": prediction.tolist()}
