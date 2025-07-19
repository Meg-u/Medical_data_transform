from dagster import op
import subprocess

@op
def scrape_telegram_data():
    subprocess.run(["python", "scrapers/scrape_messages.py"], check=True)

@op
def load_raw_to_postgres():
    subprocess.run(["python", "load_raw_json.py"], check=True)

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run"], check=True)

@op
def run_yolo_enrichment():
    # Placeholder for YOLO; currently does nothing
    print("YOLO enrichment not yet implemented.")
