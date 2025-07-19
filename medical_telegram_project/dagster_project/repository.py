# dagster_project/repository.py
from dagster import repository
from .jobs import telegram_pipeline_job
from .schedules import daily_scrape_schedule


@repository
def telegram_repo():
    return [telegram_pipeline_job]

@repository
def telegram_repo():
    return [telegram_pipeline_job, daily_scrape_schedule]
