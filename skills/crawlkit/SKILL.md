---
name: crawlkit
description: Get structured data from Booking.com, Airbnb, Amazon reviews, AliExpress, Google Shopping, Zillow, Indeed, Yelp, Reddit, Google Jobs, Google News, Google Flights, Shopify stores, public Telegram channels and Bing/DuckDuckGo with the CrawlKit scrapers on Apify. Use when the user asks for hotel or rental prices, product prices or reviews, real-estate listings, job listings, business reviews, subreddit posts, news articles, flight offers, a Shopify catalog, Telegram channel messages or search results as data.
---

# CrawlKit scrapers

Fifteen web scrapers (Apify Actors) that return clean JSON. Each run is billed per result to the user's Apify account (pay per result, no subscription; the price is shown on each Actor's page).

## Before running anything

1. You need an Apify API token. Read it from the `APIFY_TOKEN` environment variable. If it is missing, ask the user to create one at https://console.apify.com/settings/integrations; never invent or hard-code a token.
2. Pick the Actor from the table below. Always set a small limit first (10–20 results) unless the user asked for more: every result is billed.

## Run an Actor and get the results (one call)

```bash
curl -s -X POST "https://api.apify.com/v2/acts/sweet_stickball~<actor>/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '<input JSON>'
```

```python
import os, httpx
items = httpx.post(
    "https://api.apify.com/v2/acts/sweet_stickball~reddit-scraper/run-sync-get-dataset-items",
    headers={"Authorization": f"Bearer {os.environ['APIFY_TOKEN']}"},
    json={"subreddit": "webscraping", "sort": "new", "maxItems": 10},
    timeout=320,
).json()
```

- The response is the list of result objects.
- The Actor id uses `~` (`sweet_stickball~reddit-scraper`); `sweet_stickball/reddit-scraper` returns 404 on the API.
- The sync call waits up to 300 s. For large jobs, start the run with `POST /v2/acts/sweet_stickball~<actor>/runs`, poll `GET /v2/actor-runs/<runId>` until `status` is `SUCCEEDED` / `FAILED`, then read `GET /v2/datasets/<defaultDatasetId>/items`.
- A failed run explains itself in `statusMessage` (e.g. "Product … not found", "Departure date … is in the past"): report it to the user instead of retrying blindly.

## Actors and inputs

`*` = required. Dates are `YYYY-MM-DD` and must be in the future.

| Actor | Use it for | Input |
|---|---|---|
| `booking-scraper` | Hotels in a city with prices for given dates, rating, stars, address | `location` ("Paris, France") or `url` (a Booking.com search URL), `checkIn`, `checkOut`, `currency` ("EUR"), `maxItems`. Without dates Booking.com returns no prices |
| `airbnb-scraper` | Airbnb stays in a destination: price per night, total, rating, room type, beds | `location`* ("Lisbon, Portugal"), `checkIn`, `checkOut`, `currency` ("EUR"), `maxItems` |
| `amazon-reviews-scraper` | Reviews of one Amazon product | `productUrl`* (product URL or ASIN), `country` (US, UK, FR, DE, CA, JP, AU, ES, IT), `sortBy` (recent, helpful), `filterByStar` (all, five_star … one_star), `maxReviews` |
| `aliexpress-scraper` | AliExpress products: price, discount, orders, rating, seller, shipping | `query` (search) or `productUrl`, `shipTo` ("US"), `maxItems` |
| `google-shopping-scraper` | Product offers on Google Shopping: price, seller, rating, link | `query`*, `country` (us, uk, fr, de, es, it, ca, au, jp, br, in, nl), `minPrice`, `maxPrice`, `sortBy` (relevance, price_low, price_high, review_score), `maxItems` |
| `zillow-scraper` | Homes for sale or rent: price, beds, baths, area, address | `searchQuery`* ("Austin, TX"), `listingType` (sale, rent), `maxItems` |
| `reddit-scraper` | Posts of a subreddit, or comments of a post | `subreddit`* (name, subreddit URL or post URL), `sort` (hot, new, top, rising), `topPeriod` (hour … all, with `top`), `maxItems` |
| `google-jobs-scraper` | Job listings: title, company, location, salary, apply links | `query`* ("data analyst"), `location`, `language` ("en"), `maxItems` |
| `indeed-job-scraper` | Indeed job listings: title, company, location, salary, date | `query`*, `location`, `country` (US, UK, FR, DE, CA, AU), `maxItems` |
| `yelp-scraper` | One Yelp business (details) and its reviews | `businessUrl` (a yelp.com/biz URL) or `query` + `location` (resolves the **top** match only), `maxReviews` |
| `google-news-scraper` | News articles: title, source, date, link | `query`*, `language` ("en"), `country` ("US"), `maxItems` |
| `google-flights-scraper` | Flight offers: airline, price, times, stops | `origin`*, `destination`* (IATA codes: "JFK", "CDG"), `date`, `returnDate`, `travelClass` (economy, premium_economy, business, first), `stops` (any, nonstop, one_stop, two_plus), `maxResults` |
| `shopify-store-scraper` | Product catalog of a Shopify store: prices, variants, stock | `shopUrl`* ("https://www.allbirds.com"), `maxProducts`, `includeVariants`, `analyzeStore` (adds one store-level summary item) |
| `telegram-public-channel-scraper` | Latest messages of a public Telegram channel: text, date, views, media | `channelUrl`* ("https://t.me/s/durov" or "@durov"), `maxMessages`, `includeMedia` |
| `bing-ddg-serp` | Organic search results: title, URL, snippet, position | `query`*, `engine` (ddg, bing), `maxResults` |

## Good practice

- Restate what you will run and the expected volume before large runs (more than ~100 results).
- Present results as a short table or summary; offer the raw JSON if the user wants it.
- Only public data is collected. Do not use these Actors to collect personal data the user has no legitimate reason to process.
- Actor pages (documentation, output fields, prices): `https://apify.com/sweet_stickball/<actor>`.

## Through MCP instead of HTTP

If the agent supports remote MCP servers, the same Actors are available as tools via Apify's MCP server:
`https://mcp.apify.com/?actors=sweet_stickball/booking-scraper,sweet_stickball/airbnb-scraper,sweet_stickball/amazon-reviews-scraper,sweet_stickball/aliexpress-scraper,sweet_stickball/google-shopping-scraper,sweet_stickball/zillow-scraper,sweet_stickball/reddit-scraper,sweet_stickball/google-jobs-scraper,sweet_stickball/indeed-job-scraper,sweet_stickball/yelp-scraper,sweet_stickball/google-news-scraper,sweet_stickball/google-flights-scraper,sweet_stickball/shopify-store-scraper,sweet_stickball/telegram-public-channel-scraper,sweet_stickball/bing-ddg-serp` (sign in with Apify OAuth or send `Authorization: Bearer <token>`).
