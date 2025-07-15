import os
import json
import psycopg2
from datetime import datetime

# Load secrets from .env if you have them
from dotenv import load_dotenv
load_dotenv()

PG_HOST = os.getenv("POSTGRES_HOST", "localhost")
PG_DB = os.getenv("POSTGRES_DB", "medical_db")
PG_USER = os.getenv("POSTGRES_USER", "postgres")
PG_PWD = os.getenv("POSTGRES_PASSWORD", "postgres")
PG_PORT = os.getenv("POSTGRES_PORT", "5432")

RAW_DIR = "data/raw/telegram_messages"

conn = psycopg2.connect(
    host=PG_HOST,
    port=PG_PORT,
    dbname=PG_DB,
    user=PG_USER,
    password=PG_PWD
)
cur = conn.cursor()

# Create raw table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    message_id BIGINT PRIMARY KEY,
    channel_id BIGINT,
    channel_name TEXT,
    message_date TIMESTAMP,
    message_text TEXT,
    has_photo BOOLEAN
);
""")
conn.commit()

for root, dirs, files in os.walk(RAW_DIR):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(root, file)
            with open(json_path, "r", encoding="utf-8") as f:
                messages = json.load(f)
                for msg in messages:
                    msg_id = msg.get("id")
                    peer_id = msg.get("peer_id", {}).get("channel_id")
                    date = msg.get("date")
                    text = msg.get("message")
                    has_photo = msg.get("has_photo")
                    channel_name = file.replace(".json", "")

                    # Cast date safely
                    dt = datetime.fromisoformat(date) if date else None

                    cur.execute("""
                        INSERT INTO raw.telegram_messages (message_id, channel_id, channel_name, message_date, message_text, has_photo)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (message_id) DO NOTHING;
                    """, (msg_id, peer_id, channel_name, dt, text, has_photo))

conn.commit()
cur.close()
conn.close()

print("✅ Finished loading JSON files into raw.telegram_messages")
