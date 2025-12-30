# MCP Encryption Server

Simple MCP server with encryption tools for Claude Desktop.

## Setup

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "custom_encryption": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/jamemamjame/mcp-deployment.git",
        "mcp-server"
      ]
    }
  }
}
```

Restart Claude Desktop.

## Usage

Ask Claude to encrypt text using the `encrypt_data` tool. It reverses text and adds "JA" + "ME" wrapper.

Example: "Hello" → "JAolleHME"