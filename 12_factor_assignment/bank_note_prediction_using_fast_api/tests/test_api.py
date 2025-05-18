from fastapi.testclient import TestClient
from bank_note_prediction_using_fast_api.api.main import app


client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, World'}

def test_predict():
    test_data = {
        "variance": 1.0,
        "skewness": 2.0,
        "curtosis": 3.0,
        "entropy": 4.0
    }

    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
