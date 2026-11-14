# Construction Cost Estimation Using Machine Learning

## Project Overview

This project estimates the total construction cost of a building using Machine Learning.

The prediction is based on details such as construction area, location, building type, number of floors, bedrooms, bathrooms, material price index, labour rate and other construction-related factors.

The project uses a Python backend with a trained Random Forest model and FastAPI for making predictions.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- FastAPI
- Uvicorn
- Jupyter Notebook

## Dataset

The project uses a construction cost estimation dataset containing 12,000 records and 15 columns.

The dataset includes:
- Project year and district
- Building type
- Construction area
- Number of floors, bedrooms and bathrooms
- Construction quality
- Foundation type
- Material price index
- Labour rate per square foot
- Site condition
- Project duration
- Total construction cost (target variable)

## Data Cleaning

The dataset was inspected and validated before model training.

The checks included:
- Checking missing values
- Checking duplicate records
- Checking data types
- Checking negative numerical values
- Reviewing numerical data ranges

No missing values, duplicate records or negative numerical values were found in the final dataset.

## Machine Learning Models

Two regression models were trained and compared:

1. Linear Regression
2. Random Forest Regressor

Random Forest was selected because it performed better on the test dataset.

### Model Performance

| Model | MAE (₹) | RMSE (₹) | R² Score |
|---|---:|---:|---:|
| Linear Regression | 518,555.06 | 781,468.46 | 0.9147 |
| Random Forest | 327,204.59 | 491,500.21 | 0.9662 |

The Random Forest model achieved an R² score of 0.9662 on the test dataset.

## Project Structure

```text
internship_project/
│
├── backend/
│   └── main.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── construction_cost_model.pkl
│   └── data_preprocessor.pkl
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── model_training.ipynb
│
├── src/
│   └── data_cleaning.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/Huzefkhan1/construction-cost-estimation.git
cd construction-cost-estimation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Backend

From the project root directory, run:

```bash
python -m uvicorn main:app --reload --app-dir backend
```

The API will run at:

```text
http://127.0.0.1:8000
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Prediction API

The project provides a POST endpoint:

```text
/predict
```

Example input:

```json
{
  "year": 2025,
  "district": "Hyderabad",
  "building_type": "Independent House",
  "construction_area_sqft": 1500,
  "num_floors": 2,
  "bedrooms": 3,
  "bathrooms": 2,
  "construction_quality": "Standard",
  "foundation_type": "Shallow",
  "material_price_index": 150.0,
  "labor_rate_per_sqft": 750,
  "site_condition": "Normal",
  "project_duration_months": 10
}
```

Example response:

```json
{
  "estimated_cost_inr": 4991380
}
```

## Important Note

The dataset used in this project is synthetic. The model demonstrates a machine learning workflow and should be validated using real construction project data before being used for actual cost estimation.

## Author

Construction Cost Estimation - Internship Project
