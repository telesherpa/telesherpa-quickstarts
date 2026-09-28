# Telesherpa + CrewAI Quickstart

Verbindet einen CrewAI-Agenten über die native
[MCP-Integration](https://docs.crewai.com/en/mcp/overview) mit dem Telesherpa
MCP-Server.

## Setup

```bash
cp .env.example .env   # TELESHERPA_TOKEN und OPENAI_API_KEY eintragen
pip install -r requirements.txt
python quickstart.py
```

## Wie man an `TELESHERPA_TOKEN` kommt

Siehe [`auth-token-lifecycle.md`](https://github.com/telesherpa/skill-telesherpa-com/blob/main/telesherpa-ontology-platform/references/features/auth-token-lifecycle.md) im
[skill-telesherpa-com](https://github.com/telesherpa/skill-telesherpa-com)-Repo.

## Was das Skript macht

Definiert einen CrewAI-Agenten mit Zugriff auf alle Telesherpa-MCP-Tools und lässt
ihn eine einfache Objektabfrage als Task ausführen.
