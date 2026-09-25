from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title = "Iris ML Prediction API")
artifact = joblib.load("iris_model.pkl")

model = artifact["model"]
target_names = artifact["target_names"]

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return{
        "message": "Iris ML Prediction API is running"
    }

@app.post("/predict")
def predict(data : IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    return{
        "predicted_species" : target_names[prediction],
        "confidence" : round(float(max(probabilities)) , 4)
    }