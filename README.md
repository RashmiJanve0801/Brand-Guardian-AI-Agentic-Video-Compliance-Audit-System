
---

## ✨ Features

- 🎬 **Multimodal Analysis** — Audits both speech transcripts and on-screen OCR text
- 📋 **RAG-Powered Compliance** — Retrieves FTC and YouTube Ad rules semantically via Azure AI Search
- ⚖️ **Violation Classification** — Categorizes issues by type (e.g. FTC Disclosure) and severity (CRITICAL / WARNING)
- 🔁 **Stateful LangGraph Workflow** — Typed `VideoAuditState` with error-resilient node fallbacks
- 🚀 **Production-Ready API** — FastAPI with Pydantic validation and session-based tracking
- 📡 **Full Observability** — LangSmith agent tracing + Azure Monitor OpenTelemetry

---

## 🧰 Tech Stack

| Layer | Technologies |
|---|---|
| **Agent Orchestration** | LangGraph, LangChain |
| **LLM & Embeddings** | Azure OpenAI (GPT-4, text-embedding-3-small) |
| **Video Processing** | Azure Video Indexer, yt-dlp |
| **Knowledge Base** | Azure AI Search, PyPDF |
| **Backend API** | FastAPI, Uvicorn, Pydantic |
| **State & Storage** | Redis, PostgreSQL, Azure Blob Storage |
| **Observability** | LangSmith, Azure Monitor, OpenTelemetry |
| **Infra** | Docker, python-dotenv |

---

## 📁 Project Structure

