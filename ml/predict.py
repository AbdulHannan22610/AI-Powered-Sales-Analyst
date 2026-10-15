import joblib

model = joblib.load("models/sales_model.pkl")

def predict_sales(data):
    return model.predict(data)[0]