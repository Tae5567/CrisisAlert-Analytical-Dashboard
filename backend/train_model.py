import pandas as pd

# Load dataset
file_path = "data/cleaned_emergencies_data.csv"  
df = pd.read_csv(file_path)

# Display basic info
print(df.head())  # Show first few rows
print(df.info())  # Check for missing values and data types
