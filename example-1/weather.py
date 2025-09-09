from fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
def get_weather(city:str)->str:
    """Get the weather for a city"""
    return f"The weather in {city} is sunny"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
