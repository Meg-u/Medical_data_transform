from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/medical_project"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
