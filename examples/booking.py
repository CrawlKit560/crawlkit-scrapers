"""Scrape hotels in Paris from Booking.com via the Apify API."""
import httpx, os, time

TOKEN = os.environ["APIFY_TOKEN"]
BASE = "https://api.apify.com/v2"
ACTOR = "sweet_stickball~booking-scraper"

# Start the Actor run
run = httpx.post(
    f"{BASE}/acts/{ACTOR}/runs",
    params={"token": TOKEN},
    json={"location": "Paris", "checkIn": "2025-03-01", "checkOut": "2025-03-03", "maxItems": 10},
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
for h in items:
    print(f"{h['name']} — {h['price']} {h.get('currency', 'USD')} ★{h.get('rating', 'N/A')}")
