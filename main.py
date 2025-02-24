from fastapi import FastAPI
from pydantic import BaseModel
import joblib, pickle
import pandas as pd
import numpy as np

# load the trained model
model = pickle.load(open("trained_model.sav", 'rb'))

# define the FastAPI app
app = FastAPI()

# define the request body for input data to the model (features or independent variables)
class PredictRequest(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    
# define the response body for the output data from the model (target or dependent variable)
@app.post("/predict")
def predict(request: PredictRequest):
    data = np.array([[request.radius_mean, request.texture_mean, request.perimeter_mean, request.area_mean, request.smoothness_mean, request.compactness_mean, request.concavity_mean, request.concave_points_mean, request.symmetry_mean, request.fractal_dimension_mean]])
    prediction = model.predict(data)
    
    result_map = {
        0: "Not Diabetic",
        1: "Diabetic"
    }
    
    return {"prediction": result_map[int(prediction[0])]}

@app.get("/")
def read_root():
    return {"Welcome to the Diabetes Prediction API!"}
# Run the FastAPI app
# uvicorn main:app --reload
