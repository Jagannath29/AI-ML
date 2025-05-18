from fastapi import FastAPI
from .schema import BankNote
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.predict import predict_banknote

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To my home': f'{name}'}

@app.get('/health')
def health_check():
    return {'status': 'healthy'}

@app.post('/predict')
def predict(data: BankNote):
    prediction = predict_banknote(
        data.variance,
        data.skewness,
        data.curtosis,
        data.entropy
    )
    return {'prediction': prediction}