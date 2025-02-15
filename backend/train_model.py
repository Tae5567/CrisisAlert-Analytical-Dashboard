import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
file_path = "data/cleaned_emergencies_data.csv"  
df = pd.read_csv(file_path)

# Select relevant columns
columns_to_keep = [
    "disaster_type", "sub_region", "magnitude", "start_year", "start_month",
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
X = df.drop(columns=["start_year", "start_month", "total_deaths", "no_homeless", "no_injured"])
Y = df[["start_year", "start_month", "total_deaths", "no_affected", "no_homeless", "no_injured"]]

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

# Build the multi-output regression model
model = keras.Sequential([
    keras.Input(shape=(X_train.shape[1],)),  # Corrected input layer
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(6)  # 6 outputs now (to match Y)
])

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Train the model
history = model.fit(X_train, Y_train, epochs=50, batch_size=16, validation_data=(X_test, Y_test), verbose=1)

# Save the trained model
model.save("emergency_model.keras")

print("Model training completed and saved successfully!")

joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("Scaler and Label Encoders saved successfully!")
