# dagster_project/__init__.py
from dagster import asset, Definitions

@asset
def my_asset():
    return "Hello Dagster"

defs = Definitions(assets=[my_asset])