import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

def load_data(file_path):
    data = pd.read_csv(f"data/{file_path}")
    X = data.drop(columns=["target"])
    y = data["target"].dropna()
    return X, y

def preprocess_data(X):
    poly = PolynomialFeatures(degree=4, include_bias=False)
    poly_features = poly.fit_transform(X)
    return poly, poly_features
