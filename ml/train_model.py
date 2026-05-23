import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("e:/smart-agriculture-ai/data/yield_df.csv")

print("Dataset Shape:", df.shape)

# =========================
# FEATURES & TARGET
# =========================
X = df.drop("hg/ha_yield", axis=1)
y = df["hg/ha_yield"]

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# COLUMN TYPES
# =========================
numeric_features = [
    "Year",
    "average_rain_fall_mm_per_year",
    "pesticides_tonnes",
    "avg_temp"
]

categorical_features = ["Area", "Item"]

# =========================
# PREPROCESSOR
# =========================
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# =========================
# MODELS
# =========================
models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(),
    "Lasso": Lasso(),
    "DecisionTree": DecisionTreeRegressor(random_state=42),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42)
}

best_model = None
best_score = -np.inf

# =========================
# TRAINING LOOP
# =========================
for name, model in models.items():

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"\n{name}")
    print("MAE:", mae)
    print("R2 Score:", r2)

    if r2 > best_score:
        best_score = r2
        best_model = pipeline

# =========================
# SAVE BEST MODEL
# =========================
joblib.dump(best_model, "crop_yield_model.pkl")

print("\nBest Model Saved with R2:", best_score)