# API Documentation

## FastAPI Endpoints

### Prediction Endpoint
`POST /predict`

Predicts whether a bank note is genuine or forged based on input features.

#### Request Body
```json
{
    "variance": float,
    "skewness": float,
    "curtosis": float,
    "entropy": float
}
```

#### Response
```json
{
    "prediction": int  // 0 for fake, 1 for genuine
}
```

## API Structure
The API is organized in the following structure:

### Main API Module
Located in `bank_note_prediction_using_fast_api/api/main.py`
- Contains FastAPI application setup
- API endpoint definitions
- Error handling

### Schema Definitions
Located in `bank_note_prediction_using_fast_api/api/schema.py`
- Pydantic models for request/response validation
- Data type definitions