import pandas as pd
import json

df = pd.read_csv("alcools.csv")
df = df.dropna(subset=["ratio_eur_par_L_alcool_pur"])
df = df.sort_values("ratio_eur_par_L_alcool_pur")

data = df.to_dict(orient="records")
with open("alcools.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

print(f"✅ {len(data)} produits exportés dans alcools.json")
