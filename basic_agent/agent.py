from google.adk.agents import Agent
import requests
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset , StreamableHTTPConnectionParams

MCP_SERVER_URL="http://localhost:8001/mcp"

# Root Agent
root_agent = Agent(
    name = "basic_agent",
    model = "gemini-2.0-flash",
    description="Agent to run the MCP server",
    instruction=(
    ''' You task is to run the MCP tool addTwoNumbers or greet.'''
),
    tools=[MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=MCP_SERVER_URL,
                timeout=700,
                sse_read_timeout=700,
                terminate_on_close=False
                
            ),
            errlog=None,
            
        ),]
)