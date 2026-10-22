"""Fetch Amazon product reviews via the Apify API."""
import httpx, os, time

TOKEN = os.environ["APIFY_TOKEN"]
BASE = "https://api.apify.com/v2"
ACTOR = "crawlkit/amazon-reviews-scraper"

# Start the Actor run
run = httpx.post(
    f"{BASE}/acts/{ACTOR}/runs",
    params={"token": TOKEN},
    json={"productUrl": "https://www.amazon.com/dp/B0BSHF7WHW", "maxItems": 20},
).json()
run_id = run["data"]["id"]

# Poll until finished
while True:
    info = httpx.get(f"{BASE}/actor-runs/{run_id}", params={"token": TOKEN}).json()["data"]
    if info["status"] in ("SUCCEEDED", "FAILED", "ABORTED"):
        break
    time.sleep(2)

# Fetch and print results
items = httpx.get(f"{BASE}/datasets/{info['defaultDatasetId']}/items", params={"token": TOKEN}).json()
for r in items:
    print(f"★{r.get('rating', '?')} — {r.get('title', 'No title')} ({r.get('date', '')})")
