import json

with open("alcools.json", encoding="utf-8") as f:
    all_data = json.load(f)

print(f"{len(all_data)} produits chargés")

# Importe et appelle directement generate_web_view
from scraper import generate_web_view
generate_web_view(all_data)
