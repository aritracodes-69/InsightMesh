import os
import vertexai
from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Required environment variables
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("REGION")
INDEX_ENDPOINT_ID = os.getenv("MATCHING_ENGINE_INDEX_ENDPOINT")
INDEX_ID= os.getenv("MATCHING_ENGINE_INDEX")  # Default to a placeholder if not set
# Validate required config
if not PROJECT_ID:
    raise ValueError("❌ Missing PROJECT_ID environment variable.")
if not INDEX_ID:
    raise ValueError("❌ Missing MATCHING_ENGINE_INDEX environment variable.")

# Initialize Vertex AI & Matching Engine
vertexai.init(project=PROJECT_ID, location=LOCATION)
aiplatform.init(project=PROJECT_ID, location=LOCATION)

# Initialize Gemini embedding model
try:
    embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load embedding model: {e}")

def query_rag_context(text: str, k: int = 3):
    """
    Embed input text and retrieve top-k relevant documents using Matching Engine.
    """
    if not text.strip():
        return "❌ RAG error: Input text is empty."

    try:
        # Generate text embedding
        embedding = embedding_model.get_embeddings([text])[0].values
        # Retrieve index
        index_endpoint = aiplatform.MatchingEngineIndexEndpoint(index_endpoint_name=INDEX_ENDPOINT_ID)
        response=index_endpoint.find_neighbors(
               deployed_index_id=INDEX_ID,
               queries=[embedding],
               num_neighbors=k
           )
        neighbors = response[0].neighbors
        if not neighbors:
                return "ℹ️ No relevant context found."
        context = "\n\n".join(
               f"• {n.datapoint.attributes.get('text', '')}" for n in neighbors
           )
        return f"🔍 Relevant info retrieved for: '{text}'\n\n{context}"

    except Exception as e:
        return f"❌ RAG error: {str(e)}"


