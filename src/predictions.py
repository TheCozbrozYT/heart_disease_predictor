import numpy as np
from sklearn.preprocessing import StandardScaler

def make_prediction(model, poly, input_features):
    input_poly = poly.transform([input_features])
    scaler = StandardScaler()
    scaler.fit(input_poly)  # Fit on polynomial features
    input_scaled = scaler.transform(input_poly)
    prediction = model.predict_proba(input_scaled)
    return prediction[0, 1]  # Return probability of class 1
