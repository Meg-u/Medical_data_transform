import psycopg2
import pandas as pd

# Load detection results from CSV
df = pd.read_csv('data/processed/image_detections.csv')

# Database connection settings
DB_NAME = "medical_project"
DB_USER = "postgres"  
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL and insert data
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO stg_image_detections_raw (message_id, image_name, detected_class, confidence_score)
            VALUES (%s, %s, %s, %s)
        """, (
            row['message_id'],
            row['image_name'],
            row['detected_class'],
            row['confidence_score']
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully into stg_image_detections_raw.")

except Exception as e:
    print("Error while connecting to PostgreSQL:", e)
