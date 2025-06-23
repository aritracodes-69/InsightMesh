import os
from google.cloud import bigquery
from dotenv import load_dotenv

# Load from .env if present (useful for local development)
load_dotenv()

# Fetch required environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("BQ_DATASET")
TABLE_NAME = os.getenv("BQ_TABLE")
FULL_TABLE_NAME = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}" 
bq_client=bigquery.Client()
# Validate environment variables early
if not PROJECT_ID:
    raise EnvironmentError("Missing PROJECT_ID environment variable. Please set it in .env or environment config.")

def log_to_db(data: dict) -> bool:
    """
    Logs feedback data to BigQuery. Returns True if successful, else False.
    """
    try:
       errors= bq_client.insert_rows_json(FULL_TABLE_NAME, [data])

       if errors == []:
           return True
       else:
           print(f"Errors while inserting rows: {errors}")
           return False
    except Exception as e:
        print(f"Error while logging to BigQuery: {e}")
        return False

