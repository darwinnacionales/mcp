from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

import asyncio

async def main():
    mcp_client=MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools = await mcp_client.get_tools()
    model=ChatOpenAI(
        model = "gpt-4.1-mini",
        temperature = 0,
        max_tokens = None,
        timeout = None,
        max_retries = 3,
    )

    agent=create_react_agent(model,tools)

    math_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is 2 + 2?"}]})
    print("Math response: ", math_response["messages"][-1].content)
    
    weather_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in Tokyo?"}]})
    print("Weather response: ", weather_response["messages"][-1].content)

asyncio.run(main())