# Getting Started with CrawlKit Actors

This guide shows you how to run any CrawlKit Actor using the Apify REST API. No SDK needed — just HTTP requests.

## 1. Get an API Token

1. Create a free account at [apify.com](https://apify.com).
2. Go to **Settings → Integrations** ([direct link](https://console.apify.com/account#/integrations)).
3. Copy your **Personal API token**.
4. Export it as an environment variable:

```bash
export APIFY_TOKEN="apify_api_XXXXXXXXXXXXXXXXXXXXXXXX"
```

## 2. Choose an Actor

Browse all CrawlKit Actors on the [Apify Store](https://apify.com/sweet_stickball). Each Actor has a README with the full input schema and output example.

## 3. Run via API

Every Actor follows the same three-step pattern: **start → poll → read**.

### With curl

```bash
# Start a run
RUN_ID=$(curl -s -X POST \
  "https://api.apify.com/v2/acts/sweet_stickball~booking-scraper/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"location":"Paris","maxItems":5}' | jq -r '.data.id')

# Wait for completion (simple loop)
while true; do
  STATUS=$(curl -s "https://api.apify.com/v2/actor-runs/$RUN_ID?token=$APIFY_TOKEN" | jq -r '.data.status')
  echo "Status: $STATUS"
  [ "$STATUS" = "SUCCEEDED" ] || [ "$STATUS" = "FAILED" ] && break
  sleep 3
done

# Fetch results
DATASET_ID=$(curl -s "https://api.apify.com/v2/actor-runs/$RUN_ID?token=$APIFY_TOKEN" | jq -r '.data.defaultDatasetId')
curl -s "https://api.apify.com/v2/datasets/$DATASET_ID/items?token=$APIFY_TOKEN" | jq '.'
```

### With Python (httpx)

See the [examples/](../examples/) directory for complete, runnable scripts. The pattern is the same:

```python
import httpx, os, time

TOKEN = os.environ["APIFY_TOKEN"]
BASE = "https://api.apify.com/v2"

# 1. Start
run = httpx.post(f"{BASE}/acts/sweet_stickball~booking-scraper/runs",
    params={"token": TOKEN}, json={"location": "Paris", "maxItems": 5}).json()
run_id = run["data"]["id"]

# 2. Poll
while True:
    info = httpx.get(f"{BASE}/actor-runs/{run_id}", params={"token": TOKEN}).json()["data"]
    if info["status"] in ("SUCCEEDED", "FAILED", "ABORTED"):
        break
    time.sleep(2)

# 3. Read
items = httpx.get(f"{BASE}/datasets/{info['defaultDatasetId']}/items",
    params={"token": TOKEN}).json()
print(f"Got {len(items)} results")
```

## 4. Reading Results

Results are stored in a **dataset** — an append-only list of JSON objects.

### Pagination

For large datasets, use `limit` and `offset`:

```
GET /v2/datasets/{id}/items?token=...&limit=100&offset=0
GET /v2/datasets/{id}/items?token=...&limit=100&offset=100
```

### Export formats

Add `&format=csv` or `&format=xlsx` to get results as CSV or Excel:

```
GET /v2/datasets/{id}/items?token=...&format=csv
```

### Clean output

Add `&clean=true` to remove empty fields and internal metadata:

```
GET /v2/datasets/{id}/items?token=...&clean=true
```

## 5. Error Handling

- **FAILED** status: check `info["statusMessage"]` for the error reason.
- **Rate limits**: the API returns `429` if you exceed the rate limit. Back off and retry.
- **Timeouts**: for large scrapes, the Actor may run for several minutes. Keep polling.
- **Input validation**: if the input doesn't match the schema, the Actor fails immediately. Check the Actor's README for the correct input format.

## Next Steps

- [MCP Integration](mcp_integration.md) — use CrawlKit Actors from Claude, Cursor and other AI agents
- [Pricing](pricing.md) — pay-per-result model and volume discounts
