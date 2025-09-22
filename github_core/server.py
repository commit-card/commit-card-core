from mcp.server.fastmcp import FastMCP
from github_core.commit_card_github_tools.tools.public_api_tools.standard_tools import initialise_standard_tools

mcp = FastMCP(
    name="GitHub Tools",
    instructions="""    
        This MCP is equipped with tools to interact with GitHub. 
        You can fetch public repositories, pull requests, and issues for a given GitHub username.
    """,
    host="127.0.0.1",
    port=9000,
    log_level="INFO"
)

initialise_standard_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="sse")
