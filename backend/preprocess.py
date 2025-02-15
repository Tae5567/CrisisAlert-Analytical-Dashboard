import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Display basic info
#print(df.head())  # Show first few rows
#print(df.info())  # Check for missing values and data types

# Load dataset
file_path = "data/cleaned_emergencies_data.csv"  
df = pd.read_csv(file_path)

# Rename columns for easier access
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Drop unnecessary columns (keeping only relevant ones)
df = df[[
    "start_year", "start_month", "end_year", "end_month",
    "disaster_group", "disaster_sub_group", "disaster_type",
    "region", "sub_region", "magnitude", "total_deaths", "no_injured", "no_affected"
]]

# Handle missing values
df.fillna({
    "start_month": 0,
    "end_month": 0,
    "magnitude": df["magnitude"].median(),  # Replace with median
    "total_deaths": df["total_deaths"].median(),
    "no_injured": df["no_injured"].median(),
    "no_affected": df["no_affected"].median(),
}, inplace=True)

# Encode categorical variables
label_encoders = {}
categorical_columns = ["disaster_group", "disaster_sub_group", "disaster_type", "region", "sub_region"]

for col in categorical_columns:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

# Features & Target
features = ["start_year", "start_month", "disaster_group", "disaster_sub_group", "disaster_type", "region", "sub_region"]
target = "total_deaths"  

X = df[features]
y = df[target]

# Normalize numerical values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save cleaned dataset for training
df.to_csv("data/preprocessed_data.csv", index=False)

print("Preprocessing complete. Cleaned dataset saved.")