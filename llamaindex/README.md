# Telesherpa + LlamaIndex Quickstart

⚠️ **Status: Skelett, nicht verifiziert.** `llama-index-tools-mcp` unterstützt
`BasicMCPClient` für Streamable-HTTP- und SSE-Verbindungen, aber die öffentliche
Doku zeigt keinen dokumentierten `headers`-Parameter für Bearer-Token-Auth.

**TODO vor Veröffentlichung:**
1. Prüfen, ob `BasicMCPClient` einen `headers`/`auth`-Parameter akzeptiert
   (ggf. im Quellcode statt nur in der Doku nachsehen).
2. Falls nicht: klären, ob sich ein `httpx.AsyncClient` mit Auth-Header
   injizieren lässt.
3. Gegen den echten Telesherpa-Server testen, diesen Hinweis danach entfernen.

## Setup (sobald verifiziert)

```bash
cp .env.example .env
pip install -r requirements.txt
python quickstart.py
```
