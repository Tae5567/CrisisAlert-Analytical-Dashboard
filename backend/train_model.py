import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler

# Load dataset
file_path = "data/cleaned_emergencies_data.csv"
df = pd.read_csv(file_path)

# Select relevant columns
columns_to_keep = [
    "disaster_type", "sub_region",
    "start_year", "start_month", "end_year", "end_month",
    "total_deaths", "no_affected", "no_homeless", "no_injured"
]
df = df[columns_to_keep]

# Handle missing values (fill NaN with 0 for numerical columns)
df.fillna(0, inplace=True)

# Encode categorical variables
label_encoders = {}
for col in ["disaster_type", "sub_region"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define input (X) and output (Y) variables
X = df[["disaster_type", "sub_region"]]
Y = df[[
    "start_year", "start_month", "end_year", "end_month",
    "total_deaths", "no_affected", "no_homeless", "no_injured"
]]

# Scale input features (X)
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X)

# Use MinMaxScaler for year columns (2025-2040 range)
year_scaler = MinMaxScaler(feature_range=(2025, 2040))
Y[["start_year", "end_year"]] = year_scaler.fit_transform(Y[["start_year", "end_year"]])

# Scale the remaining outputs (Y) with StandardScaler
scaler_Y = StandardScaler()
Y_scaled = scaler_Y.fit_transform(Y)

# Save scalers and encoders
joblib.dump(scaler_X, "scaler_X.pkl")
joblib.dump(year_scaler, "year_scaler.pkl")
joblib.dump(scaler_Y, "scaler_Y.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

# Improved model with ReLU activation for non-negative outputs
model = keras.Sequential([
    keras.Input(shape=(X_scaled.shape[1],)),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(8, activation="relu")  # 8 outputs now
])

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Train the model
model.fit(X_scaled, Y_scaled, epochs=300, batch_size=32, validation_split=0.2)

# Save the model
model.save("emergency_model.keras")

print("✅ Model and scalers saved successfully!")
