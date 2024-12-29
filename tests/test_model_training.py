import pytest
from sklearn.linear_model import LogisticRegression
from src.model_training import train_model

def test_train_model():
    X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]
    y = [0, 1, 1, 0, 1, 0, 1, 0]
    
    model, accuracy = train_model(X, y)
    
    assert isinstance(model, LogisticRegression)
    assert 0 <= accuracy <= 1
