# Heart Disease Predictor

A machine learning project that predicts the likelihood of heart disease using patient data. This project includes data preprocessing, model training, and making predictions using a trained model, all packaged into a user-friendly structure.

## Features

- 📊 Load and preprocess heart disease datasets
- 🤖 Train machine learning models for prediction
- 🔮 Make predictions using the trained model
- 🛠️ Automated testing setup
- 📦 Easy dependency management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheCozbrozYT/heart_disease_predictor.git
cd heart_disease_predictor
```

2. Install dependencies:
```bash
python install_dependencies.py
```

Or manually install using pip:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```bash
python main.py
```

2. The program will:
   - Load the dataset from `data/heart.csv`
   - Preprocess the data
   - Train a machine learning model
   - Save the trained model to `models/heart_disease_predictor.pkl`
   - Predict heart disease likelihood for a sample input

### Testing
To ensure the code runs as expected, execute the tests:
```bash
python run_tests.py
```

## Requirements
- Python 3.6 or higher
- pandas
- numpy
- scikit-learn
- joblib
- pytest

## Project Structure
```
heart_disease_predictor/
├── main.py
├── data/
│   └── heart.csv
├── models/
│   └── heart_disease_predictor.pkl
├── src/
│   ├── data_processing.py
│   ├── model_training.py
│   └── predictions.py
├── tests/
│   ├── test_data_processing.py
│   ├── test_model_training.py
│   └── test_predictions.py
├── requirements.txt
├── install_dependencies.py
├── run_tests.py
```

## How It Works

### Data Processing
The data is loaded from `data/heart.csv` and preprocessed to generate polynomial features for better model performance.

### Model Training
A linear regression model is trained on the preprocessed data. The trained model is saved to `models/heart_disease_predictor.pkl`.

### Prediction
The program uses the trained model to predict the likelihood of heart disease based on user-provided input features.

### Testing
Automated tests in the `tests/` directory ensure that each component of the project functions correctly.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This project is for educational purposes only. The predictions made by the model are not intended for medical use. Always consult a healthcare professional for medical advice.

## Support
If you encounter any problems or have suggestions, please open an issue on the GitHub repository.

