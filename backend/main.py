
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


# Load saved model and preprocessor
model = joblib.load(MODEL_DIR / "construction_cost_model.pkl")
preprocessor = joblib.load(MODEL_DIR / "data_preprocessor.pkl")


# Create FastAPI application
app = FastAPI(title="Construction Cost Estimation API")


# Details required for cost estimation

class ConstructionDetails(BaseModel):
    year: int = Field(ge=2018, le=2025)
    district: str
    building_type: str
    construction_area_sqft: float = Field(gt=0)
    num_floors: int = Field(ge=1)
    bedrooms: int = Field(ge=1)
    bathrooms: int = Field(ge=1)
    construction_quality: str
    foundation_type: str
    material_price_index: float = Field(gt=0)
    labor_rate_per_sqft: float = Field(gt=0)
    site_condition: str
    project_duration_months: int = Field(ge=1)



# Home route
@app.get("/")
def home():
    return {"message": "Construction Cost Estimation API is running"}


# Prediction route
@app.post("/predict")
def predict_cost(details: ConstructionDetails):

    # Convert input details into a DataFrame
    project_data = pd.DataFrame([details.model_dump()])

    # Prepare data using the saved preprocessor
    prepared_data = preprocessor.transform(project_data)

    # Predict construction cost
    prediction = model.predict(prepared_data)

    return {
        "estimated_cost_inr": round(float(prediction[0]), 2)
    }
