import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Referer": "https://www.e.leclerc/cat/vins-rouges",
    "Origin": "https://www.e.leclerc",
    "Accept-Encoding": "gzip, deflate, br",
}

r = requests.get(
    "https://www.e.leclerc/api/rest/live-api/product-search",
    headers=HEADERS,
    params={
        "language": "fr-FR",
        "size": "1",
        "sorts": "[]",
        "page": "1",
        "categories": json.dumps({"code": ["NAVIGATION_vins-rouges"]}),
        "filters": json.dumps({"oaf-sign-code": {"value": ["0100", "0000"]}}),
        "pertimmContexts": "[]"
    },
    timeout=15
)

print("Status:", r.status_code)
print("Encoding:", r.encoding)
print("Content-Type:", r.headers.get("Content-Type"))
print("Réponse brute:", r.text[:1000])

# Essai de parser le JSON
try:
    data = r.json()
    item = data["items"][0]
    print("\n=== NOM ===")
    print(item.get("label"))
    print("\n=== TOUS LES ATTRIBUTS ===")
    for attr in item["variants"][0]["attributes"]:
        print(f"code: {attr.get('code'):<30} valeur: {attr.get('value')}")
    print("\n=== PRICING ===")
    print(json.dumps(item["variants"][0].get("pricing", {}), indent=2))
except Exception as e:
    print("\nErreur JSON:", e)
    print("Contenu complet:", r.content[:500])
