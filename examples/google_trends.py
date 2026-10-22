"""Get Google Trends interest-over-time data via the Apify API."""
import httpx, os, time

TOKEN = os.environ["APIFY_TOKEN"]
BASE = "https://api.apify.com/v2"
ACTOR = "sweet_stickball~google-trends-scraper"

# Start the Actor run
run = httpx.post(
    f"{BASE}/acts/{ACTOR}/runs",
    params={"token": TOKEN},
    json={"keywords": ["artificial intelligence", "machine learning"], "timeRange": "past12Months"},
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
for pt in items:
    print(f"{pt.get('date', '?')} — {pt.get('keyword', '?')}: {pt.get('value', '?')}")
