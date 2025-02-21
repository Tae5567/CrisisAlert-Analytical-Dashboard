import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf
import logging

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load model and scalers
model = tf.keras.models.load_model("emergency_model.keras")
scaler_X = joblib.load("scaler_X.pkl")
year_scaler = joblib.load("year_scaler.pkl")
scaler_Y = joblib.load("scaler_Y.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Ensure years stay within range of 2025-2040
YEAR_MIN, YEAR_MAX = 2025, 2040

# User input schema into prediction model
class PredictionInput(BaseModel):
    disaster_type: str
    sub_region: str

# Prediction endpoint
@app.post("/predict")
async def predict(input: PredictionInput):
    try:
        logging.info(f"Received Input: {input}")

        # Validate disaster_type and sub_region
        if input.disaster_type not in label_encoders["disaster_type"].classes_:
            raise HTTPException(status_code=400, detail=f"Invalid disaster_type: {input.disaster_type}")
        if input.sub_region not in label_encoders["sub_region"].classes_:
            raise HTTPException(status_code=400, detail=f"Invalid sub_region: {input.sub_region}")

        # Encode input
        disaster_type_encoded = label_encoders["disaster_type"].transform([input.disaster_type])[0]
        sub_region_encoded = label_encoders["sub_region"].transform([input.sub_region])[0]

        encoded_input = np.array([[disaster_type_encoded, sub_region_encoded]])

        logging.info(f"Encoded Input: {encoded_input}")

        # Scale input
        scaled_input = scaler_X.transform(encoded_input)
        logging.info(f"Scaled Input: {scaled_input}")

        # Model prediction
        prediction = model.predict(scaled_input)
        logging.info(f"Raw Model Output: {prediction}")

        # Inverse transform outputs
        prediction_unscaled = scaler_Y.inverse_transform(prediction)
        logging.info(f"Unscaled Prediction Output: {prediction_unscaled}")

        # Extract and reshape years for inverse transformation
        year_scaled = np.hstack([prediction[:, [0]], prediction[:, [2]]])  # (1, 2) shape
        start_year, end_year = year_scaler.inverse_transform(year_scaled)[0]

        # Clip years to valid range
        start_year = int(np.clip(start_year, YEAR_MIN, YEAR_MAX))
        end_year = int(np.clip(end_year, YEAR_MIN, YEAR_MAX))

        # Extract and clip other outputs
        start_month = int(np.clip(prediction_unscaled[0][1], 1, 12))
        end_month = int(np.clip(prediction_unscaled[0][3], 1, 12))
        total_deaths = int(max(0, prediction_unscaled[0][4]))
        no_affected = int(max(0, prediction_unscaled[0][5]))
        no_homeless = int(max(0, prediction_unscaled[0][6]))
        no_injured = int(max(0, prediction_unscaled[0][7]))

        # Return predictions
        result = {
            "predicted_start_year": start_year,
            "predicted_start_month": start_month,
            "predicted_end_year": end_year,
            "predicted_end_month": end_month,
            "predicted_total_deaths": total_deaths,
            "predicted_no_affected": no_affected,
            "predicted_no_homeless": no_homeless,
            "predicted_no_injured": no_injured,
        }

        logging.info(f"Final Prediction Result: {result}")

        return result

    except Exception as e:
        logging.error(f"Prediction Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Run FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
