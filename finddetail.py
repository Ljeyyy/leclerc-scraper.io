from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Chargement de la fiche produit...")
    page.goto("https://www.e.leclerc/pro/3760102321805", timeout=30000)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(3000)

    # Récupère tout le texte visible de la page
    content = page.content()

    # Cherche le degré d'alcool
    matches = re.findall(r'[\d,\.]+\s*%\s*[Vv]ol[^\w]', content)
    print("\n=== Degrés trouvés dans le HTML ===")
    for m in matches:
        print(m)

    # Affiche aussi les caractéristiques produit
    print("\n=== Caractéristiques visibles ===")
    elems = page.query_selector_all("*")
    for el in elems:
        try:
            txt = el.inner_text().strip()
            if "%" in txt and len(txt) < 100:
                print(repr(txt))
        except:
            pass

    browser.close()
