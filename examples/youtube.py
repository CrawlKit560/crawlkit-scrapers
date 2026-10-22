"""Extract a YouTube video transcript via the Apify API."""
import httpx, os, time

TOKEN = os.environ["APIFY_TOKEN"]
BASE = "https://api.apify.com/v2"
ACTOR = "crawlkit/youtube-transcripts"

# Start the Actor run
run = httpx.post(
    f"{BASE}/acts/{ACTOR}/runs",
    params={"token": TOKEN},
    json={"videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
).json()
run_id = run["data"]["id"]

# Poll until finished
while True:
    info = httpx.get(f"{BASE}/actor-runs/{run_id}", params={"token": TOKEN}).json()["data"]
    if info["status"] in ("SUCCEEDED", "FAILED", "ABORTED"):
        break
    time.sleep(2)

# Fetch and print transcript
items = httpx.get(f"{BASE}/datasets/{info['defaultDatasetId']}/items", params={"token": TOKEN}).json()
for seg in items:
    print(f"[{seg.get('start', 0):.1f}s] {seg.get('text', '')}")
