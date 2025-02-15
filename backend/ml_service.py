import uvicorn
import numpy as np
import tensorflow as tf
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

# Load trained model
model = tf.keras.models.load_model("emergency_model.keras")

# Load encoders and scalers
with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Define FastAPI app
app = FastAPI()

# Define input schema
class DisasterInput(BaseModel):
    disaster_type: str
    sub_region: str
    magnitude: float

# Ensure correct sub-region mapping
def map_sub_region(sub_region):
    valid_sub_regions = ["Sub-Saharan Africa", "Northern Africa"]
    return sub_region if sub_region in valid_sub_regions else "Sub-Saharan Africa"

@app.post("/predict")
def predict_disaster(input_data: DisasterInput):
    try:
        # Validate and encode categorical features
        input_data.sub_region = map_sub_region(input_data.sub_region)
        input_data.disaster_type = label_encoders["disaster_type"].transform([input_data.disaster_type])[0]
        input_data.sub_region = label_encoders["sub_region"].transform([input_data.sub_region])[0]

        # Convert input to NumPy array and scale
        input_array = np.array([[input_data.disaster_type, input_data.sub_region, input_data.magnitude]])
        input_scaled = scaler.transform(input_array)

        # Make prediction
        prediction = model.predict(input_scaled)

        # Prepare response
        response = {
            "predicted_start_year": int(prediction[0][0]),
            "predicted_start_month": int(prediction[0][1]),
            "predicted_total_deaths": int(prediction[0][2]),
            "predicted_no_affected": int(prediction[0][3]),
            "predicted_no_homeless": int(prediction[0][4]),
            "predicted_no_injured": int(prediction[0][5]),
        }
        return response

    except Exception as e:
        return {"error": str(e)}

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)