"""Telesherpa + Microsoft Agent Framework Quickstart.

STATUS: Skelett, NICHT verifiziert gegen den echten Telesherpa-Server.

Microsoft Agent Framework ist der Nachfolger von AutoGen (seit BUILD 2026).
Das Grundmuster fuer MCP-Tools ist in `autogen-ext-mcp` / dessen Nachfolger
dokumentiert, aber NICHT mit Bearer-Token-Auth gegen einen Remote-HTTP-Server
(die oeffentlichen Beispiele zeigen nur StdioServerParameters gegen lokale
MCP-Server).

TODO(Herbert): Vor dem Merge:
  1. Pruefen, welche Server-Parameter-Klasse HTTP + Auth-Header unterstuetzt.
  2. Gegen mcp.telesherpa.com testen.
  3. Diese Warnung entfernen.
"""

import os

from dotenv import load_dotenv

load_dotenv()

TELESHERPA_TOKEN = os.environ["TELESHERPA_TOKEN"]
MCP_URL = os.environ.get("TELESHERPA_MCP_URL", "https://mcp.telesherpa.com/mcp")


def main() -> None:
    raise NotImplementedError(
        "Auth-Pattern fuer Microsoft Agent Framework gegen einen Streamable-HTTP "
        "MCP-Server mit Bearer-Token ist noch nicht verifiziert. Siehe README.md "
        "fuer die offenen TODOs, bevor dieses Beispiel live geschaltet wird."
    )


if __name__ == "__main__":
    main()
