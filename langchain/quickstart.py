"""Telesherpa + LangChain Quickstart.

Verbindet einen LangChain-Agenten via `langchain-mcp-adapters` mit dem
Telesherpa MCP-Server (Streamable HTTP, Bearer-Token-Auth) und stellt eine
einfache Frage, die der Agent über die geladenen Tools beantwortet.

Auth-Pattern verifiziert gegen die offizielle langchain-mcp-adapters-Doku
(MultiServerMCPClient mit `headers`-Parameter, Transport "http").
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

TELESHERPA_TOKEN = os.environ["TELESHERPA_TOKEN"]
MCP_URL = os.environ.get("TELESHERPA_MCP_URL", "https://mcp.telesherpa.com/mcp")
MODEL = os.environ.get("QUICKSTART_MODEL", "openai:gpt-4.1")


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "telesherpa": {
                "transport": "http",
                "url": MCP_URL,
                "headers": {"Authorization": f"Bearer {TELESHERPA_TOKEN}"},
            }
        }
    )

    tools = await client.get_tools()
    print(f"{len(tools)} Telesherpa-Tools geladen.")

    agent = create_agent(MODEL, tools)
    response = await agent.ainvoke(
        {"messages": "Welche Objekttypen sind in meinem aktuellen Scope verfügbar?"}
    )
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
