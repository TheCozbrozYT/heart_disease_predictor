from src.data_processing import load_data, preprocess_data
from src.model_training import train_model, save_model
from src.predictions import make_prediction
import numpy as np

def get_user_input():
    fields = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal",
    ]
    user_input = []
    for field in fields:
        while True:
            try:
                value = float(input(f"Enter value for {field}: "))
                user_input.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
    return user_input

DATA_FILE = "data/heart.csv"
MODEL_FILE = "models/heart_disease_predictor.pkl"

if __name__ == "__main__":
    print("\nWelcome to the Heart Disease Predictor!")

    X, y = load_data(DATA_FILE)
    poly, poly_features = preprocess_data(X)

    model, accuracy = train_model(poly_features, y)
    save_model(model, MODEL_FILE)

    print("\nPlease provide the following patient details:")
    SAMPLE_INPUT = get_user_input()

    chance_of_disease = make_prediction(model, poly, SAMPLE_INPUT)[0]

    print(f"\nThis person has a {chance_of_disease * 100:.2f}% chance of having heart disease. We are {accuracy * 100:.2f}% sure.")

    if chance_of_disease > 1:
        print("This person likely DOES NOT EXIST")
    elif chance_of_disease > 0.6:
        print("This person HAS heart disease")
    elif chance_of_disease <= 0.6:
        print("This person does NOT have heart disease")
    else:
        print("This person likely DOES NOT EXIST")
