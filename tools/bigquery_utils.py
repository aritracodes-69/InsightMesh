from google.cloud import bigquery
from google.api_core.exceptions import NotFound
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
# Environment setup
PROJECT_ID = os.getenv("GCP_PROJECT", "insightmesh")
DATASET_ID = os.getenv("BQ_DATASET", "insightmesh_feedback")
TABLE_ID = os.getenv("BQ_TABLE", "feedback_records")
FULL_TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

bq_client = bigquery.Client()

# Table schema definition with partitioned timestamp
TABLE_SCHEMA = [
    bigquery.SchemaField("review_id", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("raw_feedback", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("category", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("priority", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("summary", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("action_status", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("explanation", "STRING", mode="NULLABLE"),
]


def ensure_table_exists():
    """
    Checks if the feedback_records table exists, and creates it with timestamp partitioning if not.
    """
    try:
        bq_client.get_table(FULL_TABLE_ID)
        print(f"✅ Table already exists: {FULL_TABLE_ID}")
    except NotFound:
        print(f"🛠️ Table not found. Creating: {FULL_TABLE_ID}")
        table = bigquery.Table(FULL_TABLE_ID, schema=TABLE_SCHEMA)
        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="timestamp"
        )
        bq_client.create_table(table)
        print(f"✅ Created table: {FULL_TABLE_ID}")


def insert_feedback_record(record: dict) -> bool:
    """
    Insert a preprocessed feedback record into BigQuery.
    Args:
        record (dict): Record containing review_id, timestamp, raw_feedback, etc.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        errors = bq_client.insert_rows_json(FULL_TABLE_ID, [record])
        if errors:
            print("❌ BigQuery insert errors:", errors)
            return False
        print("✅ Feedback record inserted into BigQuery.")
        return True
    except Exception as e:
        print("❌ Error inserting into BigQuery:", e)
        return False




