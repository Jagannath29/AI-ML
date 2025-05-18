# Data Structure

## Overview
This project uses the following data organization:

### Data Directories
- `data/raw/` - Original, immutable data
    - Contains `banknotes.csv` with raw bank note features
- `data/processed/` - Cleaned and processed data
    - Contains `processed_banknotes.csv` ready for modeling
- `data/interim/` - Intermediate data transformation files
- `data/external/` - Data from third party sources

## Data Description
The dataset contains features extracted from images of genuine and forged banknotes. The features include:
- Variance
- Skewness
- Curtosis
- Entropy