# Getting Started

This guide will help you set up and run the Bank Note Prediction API project.

## Prerequisites

- Python 3.12+
- pip (Python package installer)
- Git

## Installation

1. Clone the repository
```bash
git clone https://github.com/Jagannath29/fast_api_application_12_factor_principle.git
cd bank_note_prediction_using_fast_api
```

2. Create and activate a virtual environment
```bash
python -m venv newEnv
source newEnv/bin/activate  # On Linux/Mac
# or
newEnv\Scripts\activate     # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure

The project follows the cookiecutter data science structure:

```
├── data/               # All project data
│   ├── raw/           # Original, immutable data
│   ├── processed/     # Cleaned, transformed data
│   ├── interim/       # Intermediate transformations
│   └── external/      # External source data
├── models/            # Trained models
├── notebooks/         # Jupyter notebooks
└── src/              # Source code
```

## Data Setup

1. The raw data is located in `data/raw/banknotes.csv`
2. Processed data will be saved to `data/processed/processed_banknotes.csv`
3. Trained models are saved in the `models/` directory

## Running the API

1. Start the FastAPI server:
```bash
uvicorn bank_note_prediction_using_fast_api.api.main:app --reload
```

2. Access the API:
- API documentation: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## Using the API

The API provides the following endpoints:

1. Root endpoint:
```
GET /
```

2. Prediction endpoint:
```
POST /predict

Request body:
{
    "variance": float,
    "skewness": float,
    "curtosis": float,
    "entropy": float
}
```

Example using curl:
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"variance": 1.2, "skewness": -0.3, "curtosis": 2.1, "entropy": -1.5}'
```

## Development

1. Run tests:
```bash
pytest tests/
```

2. Access Jupyter notebooks:
```bash
jupyter lab
```
Navigate to `notebooks/bank_notes.ipynb` for data analysis and model development.

## Documentation

Build and serve the documentation locally:
```bash
cd docs
mkdocs serve
```

Access the documentation at http://localhost:8000
