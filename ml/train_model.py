import os

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/sample.csv")

df["total_sales"] = df["quantity"] * df["unit_price"] * (1 - df["discount"]/100)

X = df[["quantity", "unit_price", "discount"]]
y = df["total_sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = RandomForestRegressor()
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/sales_model.pkl")

print("MODEL TRAINED SUCCESSFULLY")