import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("scrapefy/fotocasa-property-scraper").call(run_input={
    "locations": ["madrid-capital"],   # place names as they appear in Fotocasa URLs
    "operation": "buy",                # or "rent"
    "propertyType": "homes",
    "minPrice": 200000,
    "maxPrice": 450000,
    "minRooms": 2,
    "maxAgeDays": 7,
    "maxItems": 100,
})

rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())
cheap = sorted(rows, key=lambda r: r["pricePerM2"] or 1e9)[:10]
for r in cheap:
    print(r["district"], r["price"], r["pricePerM2"], r["surfaceM2"])
