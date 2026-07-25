# 🤖 n8n Personal Agent

> An automated personal assistant built with **n8n**, **Python**, and **LLM-powered agents** — handling everyday tasks like calendar management, email, tasks, notes, and expense tracking through a single conversational interface.

![n8n](https://img.shields.io/badge/n8n-Workflow-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

## 📌 Overview

**n8n Personal Agent** is an AI-driven automation system that acts as a reliable executive assistant — understanding user intent, choosing the correct tool, and executing tasks accurately across multiple domains:

- 🔍 **Information Lookup** — web search for real-time, factual answers
- 📅 **Calendar Management** — create and fetch Google Calendar events
- 📧 **Email Handling** — read, summarize, and reply to Gmail messages
- ✅ **Task Management** — create, fetch, and delete Google Tasks
- 📝 **Notes** — create and append structured notes via Google Docs
- 💰 **Expense Tracking** — log and summarize expenses via Google Sheets

The agent runs on a self-hosted **n8n** instance (Docker) triggered via webhook, with a Python layer (`app.py` / `main.py`) handling external requests and testing.

---

## 🧠 How It Works

```
User Message
     │
     ▼
Webhook Trigger (n8n)
     │
     ▼
AI Agent Node ── System Prompt (sysprompt.md)
     │
     ▼
Tool Selection (Calendar / Gmail / Tasks / Docs / Sheets)
     │
     ▼
Action Executed + Response Returned
```

The agent follows a strict **system prompt** (see [`sysprompt.md`](./sysprompt.md)) that governs tool selection, decision-making rules, and response style — ensuring it never hallucinates actions and always confirms destructive operations (like deleting a task) before executing them.

---

## 🗂️ Project Structure

| File | Description |
|---|---|
| `Personal Agent.json` | Exported n8n workflow — import directly into your n8n instance |
| `app.py` | Main application entry point |
| `main.py` | Core execution logic |
| `sysprompt.md` | System prompt defining agent role, tools, and behavior rules |
| `test_webhook.py` | Script for testing webhook endpoints locally |
| `pyproject.toml` / `uv.lock` | Python dependency management (via `uv`) |

---

## ⚙️ Tech Stack

| Layer | Tool |
|---|---|
| Automation Engine | [n8n](https://n8n.io) (self-hosted via Docker) |
| AI / LLM Layer | LLM Agent (tool-calling) |
| Backend | Python |
| Dependency Management | `uv` |
| Integrations | Google Calendar · Gmail · Google Tasks · Google Docs · Google Sheets |

---

## 🚀 Getting Started

### Prerequisites
- Docker (for self-hosted n8n)
- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv) package manager
- Google Cloud OAuth credentials (Calendar, Gmail, Tasks, Docs, Sheets APIs enabled)

### Setup

```bash
# Clone the repository
git clone https://github.com/AliRaza-Dev678/n8n-Personal-Agent.git
cd n8n-Personal-Agent

# Install Python dependencies
uv sync

# Run the app
python app.py
```

### Import the n8n Workflow
1. Open your n8n instance
2. Go to **Workflows → Import from File**
3. Select `Personal Agent.json`
4. Configure your Google service credentials in each node
5. Activate the workflow

---

## 🧩 Example Use Cases

- *"What's on my calendar today?"* → Fetches and summarizes today's events
- *"Add a task: finish client proposal by Friday"* → Creates a Google Task
- *"Summarize my unread emails"* → Reads and condenses inbox activity
- *"Log an expense: 2000 PKR for groceries"* → Adds entry to Google Sheets

---

## 🛣️ Roadmap

- [ ] Add WhatsApp integration for direct messaging
- [ ] Expand memory/context retention across sessions
- [ ] Add voice input support
- [ ] Multi-user support with isolated data scopes

---

## 👤 Author

**Ali Raza**
Building intelligent AI systems — RAG · LLM Engineering · Agentic AI
[GitHub](https://github.com/AliRaza-Dev678) · [LinkedIn](#)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <i>⭐ If you find this project useful, consider giving it a star!</i>
</p>
