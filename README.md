# CrawlKit Scrapers

<!-- Logo placeholder: replace with your actual logo URL -->
<!-- ![CrawlKit Logo](https://your-cdn.com/crawlkit-logo.png) -->

[![Apify Store](https://img.shields.io/badge/Apify_Store-crawlkit-blue?logo=apify)](https://apify.com/sweet_stickball)
[![MCP](https://img.shields.io/badge/MCP-mcp.apify.com-green)](https://mcp.apify.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**24 production scrapers for e-commerce, travel, real estate, jobs, social media, finance and more.** All Actors run on [Apify](https://apify.com) — no infrastructure to manage, pay per result.

## Quick Start

```bash
pip install httpx
export APIFY_TOKEN="your_api_token_here"
python examples/booking.py
```

Get your API token at [console.apify.com/account#/integrations](https://console.apify.com/account#/integrations).

## Actors

### E-commerce

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [AliExpress Scraper](https://apify.com/sweet_stickball/aliexpress-scraper) | $0.0063 | Product search: title, price, discount, rating, store |
| [Amazon Reviews Scraper](https://apify.com/sweet_stickball/amazon-reviews-scraper) | $0.0042 | Product reviews: rating, text, date, verified — 9 marketplaces |
| [Google Shopping Scraper](https://apify.com/sweet_stickball/google-shopping-scraper) | $0.0024 | Shopping results: prices, sellers, ratings — 12 countries |
| [Shopify Scraper](https://apify.com/sweet_stickball/shopify-store-scraper) | $0.0007 | Store products: prices, variants, stock, images, tags |
| [Walmart Scraper](https://apify.com/sweet_stickball/walmart-scraper) | $0.0031 | Product search/pages: price, rating, seller, availability |

### Travel

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [Airbnb Scraper](https://apify.com/sweet_stickball/airbnb-scraper) | $0.0028 | Search results: listing, price, rating, reviews, room type |
| [Booking.com Scraper](https://apify.com/sweet_stickball/booking-scraper) | $0.0035 | Hotel search: name, price, rating, stars, district, coordinates |
| [Google Flights Scraper](https://apify.com/sweet_stickball/google-flights-scraper) | $0.00017 | Flight fares: price, airline, times, duration, stops |

### Real Estate

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [Realtor.com Scraper](https://apify.com/sweet_stickball/realtor-scraper) | $0.0007 | Property listings: price, beds, baths, sqft, coordinates |
| [Zillow Scraper](https://apify.com/sweet_stickball/zillow-scraper) | $0.0016 | Listings: price, Zestimate, beds, baths, sqft |

### Jobs

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [Google Jobs Scraper](https://apify.com/sweet_stickball/google-jobs-scraper) | $0.0063 | Job listings: title, company, location, salary, apply links |
| [Indeed Jobs Scraper](https://apify.com/sweet_stickball/indeed-job-scraper) | $0.0005 | Job listings: title, company, salary — 6 countries |
| [Glassdoor Scraper](https://apify.com/sweet_stickball/glassdoor-scraper) | $0.0023 | Company reviews + salary ranges by title |

### Social Media

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [Reddit Scraper](https://apify.com/sweet_stickball/reddit-scraper) | $0.0028 | Subreddit posts/comments: title, text, author, date |
| [Telegram Channel Scraper](https://apify.com/sweet_stickball/telegram-public-channel-scraper) | $0.0035 | Public channel messages: text, dates, views, media |
| [YouTube Transcript Scraper](https://apify.com/sweet_stickball/youtube-transcripts) | $0.0035 | Video transcripts with timestamps + metadata + comments |

### Reviews

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [App Store Reviews Scraper](https://apify.com/sweet_stickball/app-store-reviews-scraper) | $0.00007 | iOS + Google Play reviews: text, rating, date, app version |
| [Trustpilot Reviews Scraper](https://apify.com/sweet_stickball/trustpilot-reviews) | $0.00048 | Reviews + company TrustScore, review count |
| [Yelp Scraper](https://apify.com/sweet_stickball/yelp-scraper) | $0.0035 | Business reviews: name, address, rating, review text |

### Finance

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [SEC EDGAR & Yahoo Finance](https://apify.com/sweet_stickball/sec-edgar-yahoo-finance) | $0.00035 | SEC filings (10-K, 10-Q, 8-K) + stock quotes + financials |

### Search & Tech

| Actor | Price/result | Description |
|-------|-------------|-------------|
| [Bing & DuckDuckGo SERP](https://apify.com/sweet_stickball/bing-ddg-serp) | $0.0031 | Search results: titles, URLs, snippets, positions |
| [Google News Scraper](https://apify.com/sweet_stickball/google-news-scraper) | $0.0028 | News articles: headlines, sources, dates, URLs |
| [Google Trends Scraper](https://apify.com/sweet_stickball/google-trends-scraper) | $0.0021 | Interest over time + related queries, up to 5 keywords |
| [Tech Stack Detector](https://apify.com/sweet_stickball/tech-stack-scanner) | $0.0016 | Website tech stack: CMS, frameworks, analytics, CDN, hosting |

## MCP Integration

All CrawlKit Actors are available through the **Apify MCP server**, making them callable by AI agents (Claude, Cursor, etc.) with zero code.

Endpoint: `https://mcp.apify.com`

See [tutorials/mcp_integration.md](tutorials/mcp_integration.md) for setup instructions.

## Examples

| File | What it does |
|------|-------------|
| [booking.py](examples/booking.py) | Scrape hotels in Paris from Booking.com |
| [amazon_reviews.py](examples/amazon_reviews.py) | Fetch product reviews from Amazon |
| [youtube.py](examples/youtube.py) | Extract a video transcript from YouTube |
| [google_trends.py](examples/google_trends.py) | Get interest-over-time data for keywords |
| [zillow.py](examples/zillow.py) | Scrape real estate listings from Zillow |

All examples use `httpx` + the Apify REST API. No SDK required.

## Tutorials

- [Getting Started](tutorials/getting_started.md) — API token, first run, reading results
- [MCP Integration](tutorials/mcp_integration.md) — Connect CrawlKit to Claude, Cursor and other AI agents
- [Pricing](tutorials/pricing.md) — Pay-per-result model, tiers, volume discounts

## License

MIT
