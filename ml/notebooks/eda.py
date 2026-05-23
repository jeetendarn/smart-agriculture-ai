import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

# LOAD DATA
df = pd.read_csv("e:/smart-agriculture-ai/data/yield_df.csv")

print("\n--- DATA HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATES ---")
print(df.duplicated().sum())

print("\n--- SHAPE ---")
print(df.shape)

print("\n--- STATISTICS ---")
print(df.describe())

# =========================
# BASIC ANALYSIS
# =========================

print("\n--- UNIQUE COUNTRIES ---")
print(len(df['Area'].unique()))

print("\n--- UNIQUE CROPS ---")
print(len(df['Item'].unique()))

# =========================
# VISUALIZATION 1
# =========================

plt.figure(figsize=(12,6))
sns.countplot(y=df['Area'])
plt.title("Country Distribution")
plt.show()

# =========================
# VISUALIZATION 2
# =========================

plt.figure(figsize=(12,6))
sns.countplot(y=df['Item'])
plt.title("Crop Distribution")
plt.show()

# =========================
# COUNTRY YIELD ANALYSIS
# =========================

country = df['Area'].unique()
yield_per_country = []

for c in country:
    yield_per_country.append(df[df['Area'] == c]['hg/ha_yield'].sum())

plt.figure(figsize=(12,6))
sns.barplot(y=country, x=yield_per_country)
plt.title("Yield per Country")
plt.show()

# =========================
# CROP YIELD ANALYSIS
# =========================

crops = df['Item'].unique()
yield_per_crop = []

for crop in crops:
    yield_per_crop.append(df[df['Item'] == crop]['hg/ha_yield'].sum())

plt.figure(figsize=(12,6))
sns.barplot(y=crops, x=yield_per_crop)
plt.title("Yield per Crop")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY")