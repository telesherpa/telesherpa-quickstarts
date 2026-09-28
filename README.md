# Telesherpa Quickstarts

Lauffähige Minimalbeispiele, die einen Agenten in eurem Framework gegen den
[Telesherpa MCP-Server](https://github.com/telesherpa/telesherpa-mcp)
(`https://mcp.telesherpa.com`) sprechen lassen. Jedes Verzeichnis ist eigenständig
lauffähig: `.env` ausfüllen, `pip install -r requirements.txt`, Skript starten.

Für den vollen Funktionsumfang der Plattform (Objektmodell, Scopes, Automatisierung,
strukturierte Bildablage, Formulare, Self-Provisioning, ...) siehe das Guide-Repo
[skill-telesherpa-com](https://github.com/telesherpa/skill-telesherpa-com).

## Frameworks

| Framework | Verzeichnis | Status |
| --- | --- | --- |
| [LangChain](https://github.com/langchain-ai/langchain-mcp-adapters) | [`/langchain`](./langchain) | ✅ verifiziertes Auth-Pattern (Bearer-Header via `MultiServerMCPClient`) |
| [CrewAI](https://docs.crewai.com/en/mcp/overview) | [`/crewai`](./crewai) | ✅ verifiziertes Auth-Pattern (Bearer-Header via `MCPServerHTTP`) |
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/) (Nachfolger von AutoGen) | [`/agent-framework`](./agent-framework) | ⚠️ Skelett — Bearer-Auth gegen Streamable-HTTP-MCP noch zu verifizieren |
| [LlamaIndex](https://developers.llamaindex.ai/python/framework/module_guides/mcp/llamaindex_mcp/) | [`/llamaindex`](./llamaindex) | ⚠️ Skelett — Bearer-Auth-Header-Unterstützung von `BasicMCPClient` noch zu verifizieren |

Zwei der vier Beispiele (LangChain, CrewAI) nutzen ein Auth-Pattern, das in der
öffentlichen Dokumentation der jeweiligen Bibliothek eindeutig belegt und gegen den
echten Telesherpa-Server getestet ist. Bei den anderen beiden zeigt die öffentliche
Doku keinen dokumentierten Weg, einen Authorization-Header an einen Remote-MCP-Server
zu übergeben — sie sind deshalb bewusst als lauffähige **Skelette** veröffentlicht, die
beim Aufruf eine klare Fehlermeldung statt eines ungetesteten Beispiels liefern. Siehe
die Status-Hinweise in den jeweiligen Skripten.

## Voraussetzungen

Alle Beispiele brauchen:
- Einen Telesherpa-Account bzw. eine Demo-Scope mit Zugriffstoken (`TELESHERPA_TOKEN`),
  siehe [`auth-token-lifecycle.md`](https://github.com/telesherpa/skill-telesherpa-com/blob/main/telesherpa-ontology-platform/references/features/auth-token-lifecycle.md)
  im Guide-Repo für den Login-/Token-Flow
- Python 3.10–3.13 (CrewAI unterstützt 3.14 noch nicht: `requires-python <3.14`)
- Einen LLM-API-Key für das jeweilige Framework (z.B. `OPENAI_API_KEY`)

## Schnellstart in der Cloud

Dieses Repo hat eine [GitHub Codespaces](https://github.com/features/codespaces)-Konfiguration
(`.devcontainer/`) — "Code" → "Create codespace on main" reicht, keine lokale
Installation nötig.

## Mitmachen

Pull Requests für weitere Frameworks oder verbesserte Beispiele sind willkommen.
Jedes Beispiel sollte: lauffähig sein, keine echten Zugangsdaten enthalten
(`.env.example` statt `.env`), und in unter 5 Minuten vom Klonen bis zum ersten
Tool-Call führen.
