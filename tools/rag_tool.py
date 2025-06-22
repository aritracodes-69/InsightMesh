# tools/rag_tool.py
import os
import vertexai
from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
from dotenv import load_dotenv
load_dotenv()

# Environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION", "us-central1")
INDEX_ID = os.getenv("MATCHING_ENGINE_INDEX")

# Initialize Vertex AI + AI Platform
vertexai.init(project=PROJECT_ID, location=LOCATION)
aiplatform.init(project=PROJECT_ID, location=LOCATION)

# Load embedding model
embedding_model = TextEmbeddingModel.from_pretrained("textembedding-gecko@003")

def query_rag_context(text: str, k: int = 3):
    """
    Given a query text, embed it and find top-k similar documents using Matching Engine.
    """
    try:
        # Get query embedding
        embedding = embedding_model.get_embeddings([text])[0].values

        # Get Matching Engine index
        index = aiplatform.MatchingEngineIndex(index_name=INDEX_ID)

        # Query the index
        results = index.find_neighbors(queries=[embedding], num_neighbors=k)

        if not results or not results[0].neighbors:
            return "No relevant context found."

        # Extract matching text
        neighbors = results[0].neighbors
        context = "\n\n".join(
            f"• {n.datapoint.attributes.get('text', '')}" for n in neighbors
        )
        return f"🔍 Relevant info retrieved for: '{text}'\n\n{context}"

    except Exception as e:
        return f"❌ RAG error: {str(e)}"

