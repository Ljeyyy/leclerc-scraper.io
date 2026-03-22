import requests
import json

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Referer": "https://www.e.leclerc/cat/spiritueux-digestifs",
    "Origin": "https://www.e.leclerc",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

codes = [
    "NAVIGATION_champagnes-vins-effervescents",
    "NAVIGATION_champagnes",
    "NAVIGATION_vins-effervescents",
]

for code in codes:
    params = {
        "language": "fr-FR",
        "size": 5,
        "page": 1,
        "categories": json.dumps({"code": [code]}),
    }
    r = requests.get(
        "https://www.e.leclerc/api/rest/live-api/product-search",
        headers=h,
        params=params,
        timeout=15
    )
    data = r.json()
    total = data.get("total", 0)
    print(f"{code:50} → {total} produits")
