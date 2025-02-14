import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv('/Users/eyitayo/Desktop/emergency-response-dashboard/backend/data/cleaned_emergencies_data.csv')

# Keep only the necessary columns
df = df[[
    "country", "disaster_group", "disaster_sub_group", "disaster_type",
    "end_month", "end_year", "magnitude", "no_affected", "no_homeless",
    "no_injured", "region", "start_month", "start_year", "sub_region", "total_deaths"
]]

# Convert numerical columns to appropriate types, handling NaNs
numeric_columns = ["end_month", "end_year", "magnitude", "no_affected", "no_homeless", "no_injured", "start_month", "start_year", "total_deaths"]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)

# Database connection
conn = psycopg2.connect(
    dbname="emergency_db",
    user="eyitayo",
    password="",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Insert data into the database
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO emergencies (country, disaster_group, disaster_sub_group, disaster_type, 
                                 end_month, end_year, magnitude, no_affected, no_homeless, 
                                 no_injured, region, start_month, start_year, sub_region, total_deaths)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into the database.")





"""
import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv('/Users/eyitayo/Desktop/emergency-response-dashboard/backend/data/emergencies_data.csv')

import pandas as pd

df = pd.read_csv("emergencies_data.csv")

# Print actual column names in the dataset
print(df.columns)

df.rename(columns={
    "Disaster Type": "disaster_type",
    "Disaster Group": "disaster_group",
    "Disaster Subgroup": "disaster_sub_group",
    "Country": "country",
    "End Month": "end_month",
    "End Year": "end_year",
    "Magnitude": "magnitude",
    "No. Affected": "no_affected",
    "No. Homeless": "no_homeless",
    "No. Injured": "no_injured",
    "Region": "region",
    "Start Month": "start_month",
    "Start Year": "start_year",
    "Subregion": "sub_region",
    "Total Deaths": "total_deaths"
}, inplace=True)

df.to_csv("cleaned_emergencies_data.csv", index=False)  # Save cleaned file
"""