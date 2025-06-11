
# 🧠 InsightMesh

InsightMesh is a modular, multi-agent data analysis and automation system designed using **Google Cloud's Vertex AI Agent Builder (ADK)**. It enables autonomous feedback processing, classification, prioritization, and execution of intelligent actions—all orchestrated in a scalable cloud-native architecture.

---

## 🚀 Project Overview

InsightMesh is a multi-agent system that:
- Automates insight extraction from textual feedback
- Classifies, prioritizes, and routes data to business-relevant actions
- Explains decisions using Retrieval-Augmented Generation (RAG)
- Logs feedback and results to BigQuery
- Uses a modern Streamlit-based UI for interaction

---

## 🧱 Architecture

The system is composed of 7 agents:

| Agent | Function |
|-------|----------|
| **FeedbackAgent** | Analyzes user feedback sentiment |
| **ClassificationAgent** | Categorizes insights using RAG |
| **PrioritizationAgent** | Scores and ranks feedback |
| **ActionMapperAgent** | Maps insights to business actions |
| **ExecutionAgent** | Executes the mapped actions |
| **FeedbackLoggerAgent** | Logs data into BigQuery |
| **ExplainerAgent** | Generates human-readable justifications |

---

## 🗂️ Project Structure

```

insightmesh/
├── adk/                      # Reusable ADK agent/step base classes
├── agents/                   # Logic for each individual agent
├── tools/                    # Agent-specific tools and RAG functions
├── flows/                    # Agent flow orchestration YAML
├── shared/                   # Config, utils, constants
├── embeddings/               # RAG corpus prep and ingestion
├── streamlit\_ui/             # Streamlit frontend for interaction
├── tests/                    # Unit tests
├── main.py                   # Local orchestrator runner
├── Dockerfile                # For deploying Streamlit app
├── requirements.txt
└── README.md

````

---

## ☁️ Google Cloud Components Used

| Component | Purpose |
|----------|---------|
| **Vertex AI Agent Builder** | Orchestrates modular multi-agent workflows |
| **Matching Engine + RAG** | Used for grounding classification and explanations |
| **Vertex AI Embedding Model** | Generates semantic vectors |
| **BigQuery** | Stores structured logs and insights |
| **Memorystore (Redis)** | Caches session context (optional) |
| **Cloud Run** | Hosts the Streamlit frontend |

---

## 🧪 Local Development

### Prerequisites
- Python 3.9+
- GCP service account with permissions for: Vertex AI, BigQuery, Matching Engine
- Vertex AI Agent Development Kit (ADK)

### Install dependencies
```bash
pip install -r requirements.txt
````

### Run the Streamlit UI

```bash
cd streamlit_ui
streamlit run app.py
```

---

## 🔁 Deployments

* **Agents**: Deploy all 7 agents and `insightmesh_flow.yaml` using Vertex AI Agent Builder UI or SDK.
* **RAG Matching Engine**: Upload document embeddings using `embeddings/upload_to_matching_engine.py`
* **Streamlit UI**: Deploy to Cloud Run or [Streamlit Community Cloud](https://streamlit.io/cloud)

---

## 📊 BigQuery Schema (example)

* `insightmesh_dataset.feedback_logs`

```sql
feedback STRING,
sentiment STRING,
timestamp TIMESTAMP
```

* `insightmesh_dataset.insights`

```sql
timestamp TIMESTAMP,
category STRING,
priority STRING,
action STRING,
result STRING
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```
PROJECT_ID=your-gcp-project-id
LOCATION=us-central1
BIGQUERY_DATASET=insightmesh_dataset
RAG_CORPUS_ID=your-rag-corpus-id
MATCHING_ENGINE_INDEX_ID=your-index-id
```

---

## ✅ License

MIT License

---

## 🙋‍♀️ Contributions

Feel free to fork and enhance InsightMesh with new agent capabilities, more actions, integrations (Slack, Jira, Firebase), or even a mobile-friendly frontend.

---

## 🧩 TODO

* [ ] Add OpenTelemetry logging
* [ ] Add conversational memory using Redis
* [ ] Add Slack bot interface
* [ ] Add agent feedback loop for learning

---

> Designed to be modular, cloud-native, and AI-powered — **InsightMesh** transforms your feedback into actions.

