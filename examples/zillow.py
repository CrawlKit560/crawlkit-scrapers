"""Scrape Zillow real estate listings via the Apify API."""
import httpx, os, time

TOKEN = os.environ["APIFY_TOKEN"]
BASE = "https://api.apify.com/v2"
ACTOR = "crawlkit/zillow-scraper"

# Start the Actor run
run = httpx.post(
    f"{BASE}/acts/{ACTOR}/runs",
    params={"token": TOKEN},
    json={"location": "San Francisco, CA", "maxItems": 15},
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
for p in items:
    print(f"${p.get('price', '?'):,} — {p.get('beds', '?')}bd/{p.get('baths', '?')}ba — {p.get('address', 'N/A')}")
