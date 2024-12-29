import pytest
import pandas as pd
from src.data_processing import load_data, preprocess_data

def test_load_data():
    data = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [4, 5, 6, 7, 8],
        "target": [0, 1, 1, 0, 1]
    })
    data.to_csv("data/test_heart.csv", index=False)
    
    X, y = load_data("test_heart.csv")
    
    assert not X.empty
    assert not y.empty
    assert "target" not in X.columns

def test_preprocess_data():
    X = pd.DataFrame({
        "feature1": [1, 2, 3],
        "feature2": [4, 5, 6]
    })
    
    poly, poly_features = preprocess_data(X)
    
    assert poly_features.shape[1] > X.shape[1]
