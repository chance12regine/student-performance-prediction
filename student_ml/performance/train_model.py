import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor


def train():
    # Get path to this file's directory (performance/)
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / 'dataset.csv'
    model_path = base_dir / 'model.pkl'

    # Load dataset
    df = pd.read_csv(csv_path)

    # Encode categorical column
    df['Extracurricular Activities'] = LabelEncoder().fit_transform(
        df['Extracurricular Activities']
    )

    # Split features and target
    X = df.drop('Performance Index', axis=1)
    y = df['Performance Index']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, model_path)
    print("✅ Model trained and saved successfully")
