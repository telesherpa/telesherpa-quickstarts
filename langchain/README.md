# Telesherpa + LangChain Quickstart

Verbindet einen LangChain/LangGraph-Agenten über
[`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters)
mit dem Telesherpa MCP-Server.

## Setup

> Getestet mit Python 3.12 und 3.14.

```bash
cp .env.example .env   # TELESHERPA_TOKEN und OPENAI_API_KEY eintragen
pip install -r requirements.txt
python quickstart.py
```

## Wie man an `TELESHERPA_TOKEN` kommt

Siehe [`auth-token-lifecycle.md`](https://github.com/telesherpa/skill-telesherpa-com/blob/main/telesherpa-ontology-platform/references/features/auth-token-lifecycle.md) im
[skill-telesherpa-com](https://github.com/telesherpa/skill-telesherpa-com)-Repo:
`login` mit `client_id`/`client_secret` liefert ein 10h gültiges Access-Token.

## Was das Skript macht

Lädt alle für die Rolle sichtbaren Telesherpa-Tools als LangChain-Tools und lässt
einen Agenten damit eine einfache Objektabfrage beantworten.
