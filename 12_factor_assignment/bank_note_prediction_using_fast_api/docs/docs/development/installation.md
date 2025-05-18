# Installation Guide

## Prerequisites
- Python 3.12+
- pip
- virtualenv (optional but recommended)

## Setup Steps

1. Clone the repository
```bash
git clone https://github.com/Jagannath29/fast_api_application_12_factor_principle.git
cd bank_note_prediction_using_fast_api
```

2. Create and activate virtual environment (recommended)
```bash
python -m venv newEnv
source newEnv/bin/activate  # On Linux/Mac
# or
newEnv\Scripts\activate  # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Development Setup

1. Install development dependencies
```bash
pip install -r requirements-dev.txt  # if exists
```

2. Setup pre-commit hooks (if used)
```bash
pre-commit install
```

## Running the Application

1. Start the FastAPI server
```bash
uvicorn bank_note_prediction_using_fast_api.api.main:app --reload
```

2. Access the API documentation
- OpenAPI documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc