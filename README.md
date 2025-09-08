# MCP Examples Repository

This repository contains multiple examples demonstrating how to use Model Context Protocol (MCP) with different configurations and use cases.

## Example 1: Multi-Server MCP Client with Math and Weather Tools

This example demonstrates how to set up a multi-server MCP client that connects to both a local math server (via stdio) and a remote weather server (via HTTP).

### Features

- **Math Server**: Provides basic arithmetic operations (add, subtract, multiply, divide)
- **Weather Server**: Provides weather information for cities
- **Multi-Server Client**: Uses LangChain and LangGraph to create an agent that can use both servers

### Prerequisites

- Python 3.8+
- OpenAI API key (set in `.env` file)

### Setup

1. **Install dependencies**:
   ```bash
   cd example-1
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   Create a `.env` file in the `example-1` directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Start the weather server** (in a separate terminal):
   ```bash
   cd example-1
   python weather.py
   ```
   The weather server will start on `http://localhost:8000/mcp`

4. **Run the client**:
   ```bash
   cd example-1
   python client.py
   ```

### How it works

1. **Math Server** (`mathserver.py`): Runs as a stdio-based MCP server providing math operations
2. **Weather Server** (`weather.py`): Runs as an HTTP-based MCP server providing weather information
3. **Client** (`client.py`): 
   - Connects to both servers using `MultiServerMCPClient`
   - Creates a LangGraph agent with the available tools
   - Demonstrates asking math and weather questions

### Example Output

When you run `python client.py`, you should see output like:
```
Math response: 2 + 2 = 4
Weather response: The weather in Tokyo is sunny
```

### File Structure

```
example-1/
├── client.py          # Multi-server MCP client with LangGraph agent
├── mathserver.py      # Math MCP server (stdio transport)
├── weather.py         # Weather MCP server (HTTP transport)
├── main.py            # Alternative entry point
├── requirements.txt   # Python dependencies
├── pyproject.toml     # Project configuration
└── .env               # Environment variables (create this)
```

### Troubleshooting

- **OpenAI API Key**: Make sure your `.env` file contains a valid `OPENAI_API_KEY`
- **Weather Server**: Ensure the weather server is running on port 8000 before starting the client
- **Dependencies**: Make sure all packages in `requirements.txt` are installed

### Next Steps

This example demonstrates the basic setup for multi-server MCP clients. You can extend it by:
- Adding more tools to the servers
- Implementing more complex agent logic
- Adding error handling and retry mechanisms
- Creating additional MCP servers for different domains
