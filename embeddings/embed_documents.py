# Placeholder for embed_documents.py
from vertexai.language_models import TextEmbeddingModel
import json
import os

model = TextEmbeddingModel.from_pretrained("textembedding-gecko@003")

def generate_embeddings(docs):
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
    documents = ["Feedback on UI is great", "Add export to CSV feature", "App crashes when clicking save"]
    embeddings = generate_embeddings(documents)
    save_embeddings_to_file(embeddings)