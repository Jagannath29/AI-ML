import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from pathlib import Path


def train_model():
    # load data
    data_path = Path('data/raw/banknotes.csv')
    df = pd.read_csv(data_path)


    # Split features and target
    X = df.drop('class', axis =1)
    y = df['class']

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # save model
    model_path = Path("models/classifier2.pkl")
    with open(model_path, 'wb') as pkl_out:
        pickle.dump(model, pkl_out)

    return model.score(X_test, y_test)