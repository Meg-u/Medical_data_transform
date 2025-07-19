import pandas as pd
from sqlalchemy import create_engine

# Load the CSV
df = pd.read_csv("data/processed/image_detections.csv")

# Replace with your actual PostgreSQL credentials
engine = create_engine("postgresql://username:password@localhost:5432/your_database")

# Upload to PostgreSQL
df.to_sql("stg_image_detections_raw", engine, if_exists="replace", index=False)

print("CSV uploaded to PostgreSQL as stg_image_detections_raw")
