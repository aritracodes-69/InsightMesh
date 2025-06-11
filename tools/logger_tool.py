# Placeholder for logger_tool.py
from google.cloud import bigquery

import os

# Set these via environment variables or securely load them
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("BIGQUERY_DATASET") or "insightmesh_dataset"
TABLE_NAME = "feedback_logs"

def log_to_db(data):
    client = bigquery.Client(project=PROJECT_ID)
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}"
    errors = client.insert_rows_json(table_ref, [data])
    if errors:
        print("BigQuery insert errors:", errors)
        return False
    return True

def log_to_db(data):
    print("Logging to DB:", data)
    return True