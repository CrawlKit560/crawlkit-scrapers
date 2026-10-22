# MCP Integration — Connect CrawlKit to AI Agents

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) lets AI agents call external tools directly. All CrawlKit Actors are available through the **Apify MCP server** — no code needed.

## What is MCP?

MCP is an open protocol that lets AI models (Claude, GPT, etc.) discover and call tools at runtime. Instead of writing API glue code, you point your AI agent at an MCP server and it can browse available tools, understand their inputs, and call them autonomously.

## The Apify MCP Server

Apify hosts a public MCP server at:

```
https://mcp.apify.com
```

This server exposes every Actor on the Apify Store (including all CrawlKit scrapers) as callable MCP tools. The AI agent sees each Actor's name, description and input schema, and can run it with the right parameters.

## Configure in Claude Desktop

Add the Apify MCP server to your `claude_desktop_config.json`:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

Restart Claude Desktop. You should see Apify tools in the MCP tools list.

## Configure in Cursor

Add to your project's `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

Restart Cursor or reload the MCP configuration.

## Example Prompts

Once connected, you can ask your AI agent directly:

- *"Scrape the top 10 hotels in Tokyo from Booking.com for December 1-3"*
- *"Get the latest Amazon reviews for ASIN B0BSHF7WHW"*
- *"What are the Google Trends for 'electric vehicles' vs 'hybrid cars' over the past 12 months?"*
- *"Find Zillow listings in Austin, TX under $500k"*
- *"Extract the transcript of this YouTube video: https://www.youtube.com/watch?v=..."*

The agent will automatically find the right CrawlKit Actor, build the input, run it, and return the results.

## How It Works

```
User prompt
    ↓
AI Agent (Claude, Cursor, etc.)
    ↓ MCP tool call
Apify MCP Server (mcp.apify.com)
    ↓ runs Actor
CrawlKit Actor (e.g. booking-scraper)
    ↓ returns dataset
AI Agent formats & presents results
```

## Tips

- **Actor selection**: the agent picks the best Actor based on your prompt. Be specific about the data source (Booking, Zillow, Amazon, etc.) for best results.
- **Limits**: include result limits in your prompt ("top 10", "first 20 reviews") to keep runs fast and cheap.
- **Token**: keep your Apify token secure. Use environment variables or a secrets manager.
