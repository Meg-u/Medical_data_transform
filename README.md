Medical Telegram Data Platform — Kara Solutions

Overview

This project is part of my training at Kara Solutions to build a robust end-to-end data platform to generate insights about Ethiopian medical businesses.  
The pipeline collects data from public Telegram channels, stores it in a raw data lake, transforms it using dbt, and loads it into a PostgreSQL data warehouse.  

Key business questions this pipeline enables:
- What are the top 10 most mentioned medical products or drugs?
- How does price or availability vary across channels?
- Which channels have the most visual content?
- What are daily and weekly trends in posting?


- Scraper: Extracts raw Telegram messages and images.
- Data : Stores raw JSONs and images in partitioned folders.
-PostgreSQL: Acts as the data warehouse.
- DBT: Transforms raw data into a clean star schema.
- Docker: Ensures the environment is portable and reproducible.

Features Completed (Interim)

-Project environment and secrets secured with `.env` and `.gitignore`.
- Raw message scraping from multiple Telegram channels.
- Partitioned data lake with clear folder structure.
-PostgreSQL database deployed via Docker Compose.
- DBT project set up and ready to transform raw JSON to a star schema.

Next Steps

- Data Enrichment (YOLO)**: Add object detection to extract useful information from images.
- FastAPI: Build an analytical API to serve final insights.
- Pipeline Orchestration (Dagster): Automate and monitor the full workflow end-to-end.

How to Run

1. Clone the repo & install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt


Final submsion
Create your .env with your Telegram API keys.

Start Postgres:

docker-compose up -d
Scrape messages:

python src/scraping/scraper.py
python src/scraping/image_scraper.py
Load data with DBT:
dbt run

Run pipeline locally with Dagster
dagster dev

Run FastAPI API
uvicorn api.main:app --reload

Available API Endpoints
GET /api/reports/top-products?limit=10 → Most mentioned products

GET /api/channels/{channel_name}/activity → Channel posting trends

GET /api/search/messages?query=paracetamol → Search messages by keyword

Tasks Summary
Task	Description
Task 0  Environment set up
Task 1	Scrape Telegram medical data
Task 2	Load + Transform with dbt
Task 3	Image object detection via YOLOv8
Task 4	Analytical API via FastAPI
Task 5	Pipeline orchestration using Dagster







