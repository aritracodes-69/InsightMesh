# embed_documents.py
from vertexai.language_models import TextEmbeddingModel
import json
import os
import vertexai

# Initialize Vertex AI
vertexai.init(project=os.getenv("PROJECT_ID"), location=os.getenv("LOCATION", "us-central1"))

def generate_embeddings(docs):
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@003")
    embeddings = []
    for doc in docs:
        result = model.get_embeddings([doc])[0]
        embeddings.append({
            "text": doc,
            "embedding": result.values
        })
    return embeddings

def save_embeddings_to_file(embeddings, output_path="embeddings.json"):
    with open(output_path, "w") as f:
        json.dump(embeddings, f)

if __name__ == "__main__":
    documents = [
        "Feedback on UI is great",
        "Add export to CSV feature",
        "App crashes when clicking save"
    ]
    embeddings = generate_embeddings(documents)
    save_embeddings_to_file(embeddings)
