from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="LinkedIn Tools",
    instructions="""    
        This MCP is equipped with tools to interact with LinkedIn. 
        You can fetch public profiles, connections, and posts for a given LinkedIn username.
    """,
    host="127.0.0.1",
    port=9001,
    log_level="INFO"
)

if __name__ == "__main__":
    mcp.run(transport="sse")
