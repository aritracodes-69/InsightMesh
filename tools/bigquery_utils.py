from google.cloud import bigquery
import os

def get_feedback_records(dataset="Reviews", table="g01"):
    client = bigquery.Client(project=os.getenv("PROJECT_ID"))
    query = f"""
        SELECT * FROM `{os.getenv("PROJECT_ID")}.{dataset}.{table}`
        LIMIT 100
    """
    result = client.query(query)
    return [dict(row) for row in result]
