# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("jame-encryption-server", host="0.0.0.0", port=8000)


# Add an addition tool
@mcp.tool()
def encrypt_data(data: str) -> str:
    return "JA" + data[::-1] + "ME"  # Simple reversal encryption for demonstration
