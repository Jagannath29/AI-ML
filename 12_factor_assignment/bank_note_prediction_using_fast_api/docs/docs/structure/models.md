# Models

## Model Overview
The project uses machine learning models for bank note authentication prediction.

### Model Files
- `models/classifier.pkl` - The trained model for banknote prediction
- `models/classifier1.pkl` - Backup/alternative model

## Model Structure
The project's model components are organized as follows:

### Training
Located in `bank_note_prediction_using_fast_api/models/training.py`
- Handles model training pipeline
- Data preprocessing
- Model evaluation

### Prediction
Located in `bank_note_prediction_using_fast_api/models/predict.py`
- Handles real-time predictions
- Model loading and inference
- Input preprocessing