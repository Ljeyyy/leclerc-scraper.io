from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # ouvre Chrome visible
    page = browser.new_page()

    requests_log = []

    # Intercepte toutes les requêtes réseau
    def handle_response(response):
        url = response.url
        try:
            if response.status == 200 and any(x in url for x in ["search", "product", "catalog", "algolia", "elastic"]):
                body = response.json()
                print(f"\n✅ URL trouvée : {url}")
                print(json.dumps(body, indent=2, ensure_ascii=False)[:1000])
                requests_log.append({"url": url, "body": body})
        except:
            pass

    page.on("response", handle_response)

    print("Chargement de la page Leclerc vins...")
    page.goto("https://www.e.leclerc/cat/vins-rouges", timeout=30000)
    page.wait_for_timeout(8000)  # attend 8 secondes que tout charge

    print(f"\n--- {len(requests_log)} requêtes intéressantes trouvées ---")
    browser.close()
