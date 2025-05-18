FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY bank_note_prediction_using_fast_api /app/bank_note_prediction_using_fast_api
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the package
WORKDIR /app/bank_note_prediction_using_fast_api
RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "bank_note_prediction_using_fast_api.api.main:app", "--host", "0.0.0.0", "--port", "8000"]