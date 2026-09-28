# Telesherpa + Microsoft Agent Framework Quickstart

⚠️ **Status: Skelett, nicht verifiziert.** Microsoft Agent Framework ist der
Nachfolger von AutoGen (seit BUILD 2026, siehe
[Migrationsguide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)).
Das MCP-Grundmuster (`autogen-ext-mcp` bzw. dessen Nachfolge-Paket im Agent
Framework) ist belegt, aber die öffentliche Doku zeigt keinen eindeutigen Weg,
einen `Authorization`-Bearer-Header an einen Streamable-HTTP-MCP-Server zu
übergeben (die dokumentierten Beispiele nutzen `StdioServerParameters`, keinen
Remote-HTTP-Server mit Auth).

**Noch offen (dieses Beispiel ist bewusst als Skelett veröffentlicht):**
1. Prüfen, ob das Agent-Framework-Äquivalent von `SseServerParams`/`HttpServerParams`
   einen `headers`-Parameter unterstützt (analog zu LangChain/CrewAI).
2. Falls nicht dokumentiert: gegen den echten Telesherpa-Server testen, ob ein
   selbst injizierter `httpx`-Client mit Auth-Header funktioniert.
3. Diesen Hinweis entfernen, sobald das Skript real gegen `mcp.telesherpa.com` läuft.

## Setup (sobald verifiziert)

```bash
cp .env.example .env
pip install -r requirements.txt
python quickstart.py
```
