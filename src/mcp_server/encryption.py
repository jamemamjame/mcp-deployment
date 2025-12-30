# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("jame-encryption-server")


# Add an addition tool
@mcp.tool()
def encrypt_data(data: str) -> str:
    return "JA" + data[::-1] + "ME"  # Simple reversal encryption for demonstration
