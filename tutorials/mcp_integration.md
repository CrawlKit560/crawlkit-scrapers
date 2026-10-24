# MCP Integration — Connect CrawlKit to AI Agents

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) lets AI agents call external tools directly. The public CrawlKit Actors are available through Apify's hosted **MCP server**, restricted to CrawlKit — no code needed.

## What is MCP?

MCP is an open protocol that lets AI models (Claude, GPT, etc.) discover and call tools at runtime. Instead of writing API glue code, you point your AI agent at an MCP server and it can browse available tools, understand their inputs, and call them autonomously.

## The CrawlKit MCP endpoint

Apify hosts an MCP server (Streamable HTTP). The `actors` parameter restricts it to the CrawlKit Actors, so your agent only sees these tools (one per Actor, plus Apify's run and dataset helpers):

```
https://mcp.apify.com/?actors=sweet_stickball/booking-scraper,sweet_stickball/airbnb-scraper,sweet_stickball/amazon-reviews-scraper,sweet_stickball/aliexpress-scraper,sweet_stickball/google-shopping-scraper,sweet_stickball/wayfair-scraper,sweet_stickball/bestbuy-scraper,sweet_stickball/zillow-scraper,sweet_stickball/reddit-scraper,sweet_stickball/google-jobs-scraper,sweet_stickball/indeed-job-scraper,sweet_stickball/yelp-scraper,sweet_stickball/grubhub-scraper,sweet_stickball/offerup-scraper,sweet_stickball/vinted-scraper,sweet_stickball/google-news-scraper,sweet_stickball/google-flights-scraper,sweet_stickball/shopify-store-scraper,sweet_stickball/telegram-public-channel-scraper,sweet_stickball/bing-ddg-serp
```

The same endpoint is listed on the official MCP Registry as `io.github.CrawlKit560/crawlkit-scrapers` and kept in [server.json](../server.json). The AI agent sees each Actor's name, description and input schema, and can run it with the right parameters.

## Configure in Claude Desktop

Add the Apify MCP server to your `claude_desktop_config.json`:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "crawlkit": {
      "url": "https://mcp.apify.com/?actors=sweet_stickball/booking-scraper,sweet_stickball/airbnb-scraper,sweet_stickball/amazon-reviews-scraper,sweet_stickball/aliexpress-scraper,sweet_stickball/google-shopping-scraper,sweet_stickball/wayfair-scraper,sweet_stickball/bestbuy-scraper,sweet_stickball/zillow-scraper,sweet_stickball/reddit-scraper,sweet_stickball/google-jobs-scraper,sweet_stickball/indeed-job-scraper,sweet_stickball/yelp-scraper,sweet_stickball/grubhub-scraper,sweet_stickball/offerup-scraper,sweet_stickball/vinted-scraper,sweet_stickball/google-news-scraper,sweet_stickball/google-flights-scraper,sweet_stickball/shopify-store-scraper,sweet_stickball/telegram-public-channel-scraper,sweet_stickball/bing-ddg-serp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

Restart Claude Desktop. You should see the CrawlKit tools (`sweet_stickball--<actor>`) in the MCP tools list. You can also sign in with Apify OAuth instead of sending a token, if your client supports it.

## Configure in Cursor

Add to your project's `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "crawlkit": {
      "url": "https://mcp.apify.com/?actors=sweet_stickball/booking-scraper,sweet_stickball/airbnb-scraper,sweet_stickball/amazon-reviews-scraper,sweet_stickball/aliexpress-scraper,sweet_stickball/google-shopping-scraper,sweet_stickball/wayfair-scraper,sweet_stickball/bestbuy-scraper,sweet_stickball/zillow-scraper,sweet_stickball/reddit-scraper,sweet_stickball/google-jobs-scraper,sweet_stickball/indeed-job-scraper,sweet_stickball/yelp-scraper,sweet_stickball/grubhub-scraper,sweet_stickball/offerup-scraper,sweet_stickball/vinted-scraper,sweet_stickball/google-news-scraper,sweet_stickball/google-flights-scraper,sweet_stickball/shopify-store-scraper,sweet_stickball/telegram-public-channel-scraper,sweet_stickball/bing-ddg-serp",
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
- *"Find Zillow listings in Austin, TX under $500k"*
- *"Compare office chair prices on Wayfair and Best Buy"*
- *"Show the newest Nike listings on Vinted France"*

The agent will automatically find the right CrawlKit Actor, build the input, run it, and return the results.

## How It Works

```
User prompt
    ↓
AI Agent (Claude, Cursor, etc.)
    ↓ MCP tool call
Apify MCP server (mcp.apify.com/?actors=sweet_stickball/...)
    ↓ runs Actor
CrawlKit Actor (e.g. booking-scraper)
    ↓ returns dataset
AI Agent formats & presents results
```

## Tips

- **Actor selection**: the agent picks the best Actor based on your prompt. Be specific about the data source (Booking, Zillow, Amazon, etc.) for best results.
- **Limits**: include result limits in your prompt ("top 10", "first 20 reviews") to keep runs fast and cheap.
- **Token**: keep your Apify token secure. Use environment variables or a secrets manager.
