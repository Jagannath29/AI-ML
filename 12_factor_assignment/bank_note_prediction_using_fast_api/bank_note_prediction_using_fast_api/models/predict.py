import pickle
import numpy as np
from pathlib import Path
import os

# load model
def load_model():
    # Get the absolute path to the models directory
    base_path = Path(__file__).parent.parent.parent.parent
    model_path = base_path / "bank_note_prediction_using_fast_api" / "models" / "classifier.pkl"
    # open model
    with open(model_path, 'rb') as pkl_file:
        model = pickle.load(pkl_file)

    return model

# prediction
def predict_banknote(variance: float, skewness: float, curtosis: float, entrypy: float):
    # load model
    model = load_model()
    # make prediction
    prediction = model.predict([[variance, skewness, curtosis, entrypy]])

    return "Fake note" if prediction[0] > 0.5 else "It is a bank note"
