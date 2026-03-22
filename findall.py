import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.e.leclerc/cat/vins-rouges",
    "Origin": "https://www.e.leclerc",
}

r = requests.get(
    "https://www.e.leclerc/api/rest/live-api/product-search",
    headers=HEADERS,
    params={
        "language": "fr-FR", "size": "1", "sorts": "[]", "page": "1",
        "categories": json.dumps({"code": ["NAVIGATION_vins-rouges"]}),
        "filters": json.dumps({"oaf-sign-code": {"value": ["0100", "0000"]}}),
        "pertimmContexts": "[]"
    },
    timeout=15
)

item = r.json()["items"][0]

print("=== SLUG ===")
print(item.get("slug"))

print("\n=== ATTRIBUTE GROUPS ===")
print(json.dumps(item.get("attributeGroups", []), indent=2, ensure_ascii=False))

print("\n=== FAMILIES ===")
print(json.dumps(item.get("families", []), indent=2, ensure_ascii=False))

print("\n=== MERCHANDISING DATA ===")
print(json.dumps(item["variants"][0].get("merchandisingData", {}), indent=2, ensure_ascii=False))

print("\n=== ADDITIONAL FIELDS ===")
print(json.dumps(item["variants"][0]["offers"][0].get("additionalFields", {}), indent=2, ensure_ascii=False))
