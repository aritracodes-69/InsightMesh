# upload_to_matching_engine.py
from google.cloud import aiplatform
import json
import os

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION", "us-central1")
INDEX_ID = os.getenv("MATCHING_ENGINE_INDEX")

# Initialize AI Platform
aiplatform.init(project=PROJECT_ID, location=LOCATION)

# Load embedding data
with open("embeddings.json") as f:
    records = json.load(f)

# Convert to format required by Matching Engine
datapoints = [
    aiplatform.MatchingEngineIndexDatapoint(
        datapoint_id=str(i),
        feature_vector=rec["embedding"],
        restricts=None,
        crowding_tag=None,
        attributes={"text": rec["text"]}
    )
    for i, rec in enumerate(records)
]

# Get index object
index = aiplatform.MatchingEngineIndex(index_name=INDEX_ID)

# Upload the datapoints
index.upsert_datapoints(datapoints=datapoints)

print("✅ Upload completed to Matching Engine.")
