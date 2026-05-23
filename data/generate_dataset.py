import pandas as pd
import numpy as np

np.random.seed(42)

countries = ["India", "USA", "Brazil", "China", "Australia", "Nigeria", "Argentina"]
crops = ["Wheat", "Rice", "Maize", "Barley", "Soybean"]

rows = []

for year in range(1990, 2023):
    for country in countries:
        for crop in crops:

            rainfall = np.random.randint(300, 3000)
            pesticides = np.random.randint(10, 500)
            temp = round(np.random.uniform(10, 35), 2)

            # realistic yield formula (IMPORTANT improvement)
            yield_value = (
                (rainfall * 0.8) +
                (pesticides * 2) -
                (temp * 10) +
                np.random.randint(0, 1000)
            )

            rows.append({
                "Year": year,
                "Area": country,
                "Item": crop,
                "average_rain_fall_mm_per_year": rainfall,
                "pesticides_tonnes": pesticides,
                "avg_temp": temp,
                "hg/ha_yield": max(0, round(yield_value, 2))
            })

df = pd.DataFrame(rows)

df.to_csv("data/yield_df.csv", index=False)

print("Dataset created successfully!")