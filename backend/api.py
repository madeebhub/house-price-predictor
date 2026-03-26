from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os

# ------------------ Load Model ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "house_price_predictor.joblib")

model = joblib.load(MODEL_PATH)

# ------------------ App ------------------
app = FastAPI(title="House Price Prediction API")

# ------------------ CORS ------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ Input Schema ------------------
class HouseInput(BaseModel):
    bedrooms: float
    bathrooms: float
    sqft_living: float
    sqft_above: float
    sqft_basement: float
    waterfront: int
    view: int
    condition: int
    yr_built: int
    yr_renovated: int


# ------------------ Test Route (optional but helpful) ------------------
@app.get("/")
def home():
    return {"message": "House Price API running successfully"}


# ------------------ Prediction Route ------------------
@app.post("/predict")
def predict(data: HouseInput):
    try:
        features = [[
            data.bedrooms,
            data.bathrooms,
            data.sqft_living,
            data.sqft_above,
            data.sqft_basement,
            data.waterfront,
            data.view,
            data.condition,
            data.yr_built,
            data.yr_renovated
        ]]

        prediction = model.predict(features)[0]

        return {
            "predicted_price": round(float(prediction), 2)
        }

    except Exception as e:
        return {"error": str(e)}