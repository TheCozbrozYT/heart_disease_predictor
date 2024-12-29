import pytest
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from src.predictions import make_prediction

def test_make_prediction():
    X = [[1, 2], [3, 4], [5, 6]]
    y = [0, 1, 1]
    
    poly = PolynomialFeatures(degree=4, include_bias=False)
    X_poly = poly.fit_transform(X)
    
    model = LogisticRegression(random_state=42)
    model.fit(X_poly, y)
    
    input_features = [7, 8]
    prediction = make_prediction(model, poly, input_features)
    
    assert isinstance(prediction, float)
    assert 0 <= prediction <= 1
