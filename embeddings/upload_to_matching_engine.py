# Placeholder for upload_to_matching_engine.py
from google.cloud import aiplatform_matching_engine
import json
import os

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = "us-central1"
INDEX_ID = os.getenv("MATCHING_ENGINE_INDEX")

client = aiplatform_matching_engine.MatchingEngineClient()

with open("embeddings.json") as f:
    records = json.load(f)

points = [
    {
        "id": str(i),
        "embedding": rec["embedding"],
        "metadata": {"text": rec["text"]}
    } for i, rec in enumerate(records)
]

response = client.upsert_datapoints(
    index=INDEX_ID,
    datapoints=points,
    location=LOCATION,
    project=PROJECT_ID,
)

print("Upload response:", response)