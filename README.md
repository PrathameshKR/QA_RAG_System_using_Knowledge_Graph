# REASONGRAPH: Explainable Knowledge Retrieval using Graph-RAG and LLMS

A research-oriented project that combines **Knowledge Graphs**, **Large Language Models (LLMs)**, and **Graph-Based Retrieval** to build an explainable AI system for engineering knowledge retrieval.

The system extracts structured knowledge from unstructured text/PDFs, constructs a knowledge graph, performs graph traversal for reasoning, and generates explainable answers using LLMs.

---

# 🚀 Features

- 📄 PDF/Text ingestion
- 🤖 LLM-based triple extraction using Gemini
- 🧱 Knowledge Graph construction
- 🔍 Graph-based retrieval and reasoning
- 🧠 Graph-RAG answer generation
- 🛡️ Validation layer for extracted triples
- 💾 Persistent JSON-based storage
- 🔗 Explainable reasoning paths

---

# 🧠 System Architecture

```text
Input Text / PDF
        ↓
LLM-Based Extraction
        ↓
Validation Layer
        ↓
Knowledge Graph Construction
        ↓
Graph Storage
        ↓
User Query
        ↓
Graph Traversal
        ↓
Reasoning Paths
        ↓
LLM Explanation (Graph-RAG)
        ↓
Final Answer
