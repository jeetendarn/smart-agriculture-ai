import pandas as pd
import numpy as np

np.random.seed(42)

countries = ["India", "USA", "Brazil", "China", "Australia", "Nigeria", "Argentina"]
crops = ["Wheat", "Rice", "Maize", "Barley", "Soybean"]

data = []

for year in range(1990, 2023):
    for country in countries:
        for crop in crops:
            row = {
                "Year": year,
                "Area": country,
                "Item": crop,
                "average_rain_fall_mm_per_year": np.random.randint(300, 3000),
                "pesticides_tonnes": np.random.randint(10, 500),
                "avg_temp": round(np.random.uniform(10, 35), 2),
                "hg/ha_yield": np.random.randint(500, 5000)
            }
            data.append(row)

df = pd.DataFrame(data)

df.to_csv("yield_df.csv", index=False)

print("Dataset created successfully!")