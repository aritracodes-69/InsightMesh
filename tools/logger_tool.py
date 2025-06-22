import os
from google.cloud import bigquery
from dotenv import load_dotenv

# Load from .env if present (useful for local development)
load_dotenv()

# Fetch required environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("BIGQUERY_DATASET", "insightmesh_dataset")
TABLE_NAME = "feedback_logs"

# Validate environment variables early
if not PROJECT_ID:
    raise EnvironmentError("Missing PROJECT_ID environment variable. Please set it in .env or environment config.")

def log_to_db(data: dict) -> bool:
    """
    Logs feedback data to BigQuery. Returns True if successful, else False.
    """
    try:
        client = bigquery.Client(project=PROJECT_ID)
        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}"
        errors = client.insert_rows_json(table_ref, [data])

        if errors:
            print("BigQuery insert errors:", errors)
            return False
        return True

    except Exception as e:
        print(f"Error while logging to BigQuery: {e}")
        return False

