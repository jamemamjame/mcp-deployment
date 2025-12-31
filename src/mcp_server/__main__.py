from mcp_server.encryption import mcp


def main():
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
