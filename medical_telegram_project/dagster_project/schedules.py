from dagster import ScheduleDefinition
from .jobs import telegram_pipeline

daily_pipeline_schedule = ScheduleDefinition(
    job=telegram_pipeline,
    cron_schedule="0 2 * * *",  
)
