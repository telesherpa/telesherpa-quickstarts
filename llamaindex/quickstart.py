"""Telesherpa + LlamaIndex Quickstart.

STATUS: Skelett, NICHT verifiziert gegen den echten Telesherpa-Server.

`llama-index-tools-mcp` bietet BasicMCPClient fuer Streamable-HTTP/SSE, aber die
oeffentliche Doku zeigt keinen dokumentierten Weg, einen Authorization-Bearer-
Header mitzugeben.

Offen (Stand der Veroeffentlichung):
  1. Pruefen, ob BasicMCPClient einen headers-Parameter akzeptiert (ggf. Quellcode
     pruefen statt nur Doku).
  2. Gegen mcp.telesherpa.com testen.
  3. Diese Warnung entfernen, sobald das Skript real laeuft.
"""

import os

from dotenv import load_dotenv

load_dotenv()

TELESHERPA_TOKEN = os.environ["TELESHERPA_TOKEN"]
MCP_URL = os.environ.get("TELESHERPA_MCP_URL", "https://mcp.telesherpa.com/mcp")


def main() -> None:
    raise NotImplementedError(
        "Auth-Pattern fuer LlamaIndex (BasicMCPClient) gegen einen Streamable-HTTP "
        "MCP-Server mit Bearer-Token ist nicht verifiziert. Siehe README.md; "
        "dieses Beispiel ist bewusst als Skelett veroeffentlicht."
    )


if __name__ == "__main__":
    main()
