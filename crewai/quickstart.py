"""Telesherpa + CrewAI Quickstart.

Verbindet einen CrewAI-Agenten via der nativen MCP-Integration mit dem
Telesherpa MCP-Server (Streamable HTTP, Bearer-Token-Auth).

Auth-Pattern verifiziert gegen die offizielle CrewAI-MCP-Doku
(MCPServerHTTP mit `headers`-Parameter, `streamable=True`).
"""

import os

from crewai import Agent, Crew, Task
from crewai.mcp import MCPServerHTTP
from dotenv import load_dotenv

load_dotenv()

TELESHERPA_TOKEN = os.environ["TELESHERPA_TOKEN"]
MCP_URL = os.environ.get("TELESHERPA_MCP_URL", "https://mcp.telesherpa.com/mcp")

telesherpa_mcp = MCPServerHTTP(
    url=MCP_URL,
    headers={"Authorization": f"Bearer {TELESHERPA_TOKEN}"},
    streamable=True,
    cache_tools_list=True,
)

agent = Agent(
    role="Facility Analyst",
    goal="Objekte und Bildkategorien in Telesherpa abfragen und pflegen",
    backstory="Ein Agent mit Zugriff auf die Telesherpa Ontologie-Plattform via MCP.",
    mcps=[telesherpa_mcp],
)

task = Task(
    description="Welche Objekttypen sind im aktuellen Scope verfügbar? Liste sie kurz auf.",
    expected_output="Eine kurze Liste der verfügbaren Objekttypen.",
    agent=agent,
)

if __name__ == "__main__":
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    print(result)
