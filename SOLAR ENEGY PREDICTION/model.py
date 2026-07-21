import pickle
from pathlib import Path

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'solar_dataset.csv' if (BASE_DIR / 'solar_dataset.csv').exists() else BASE_DIR / 'spg.csv'
MODEL_PATH = BASE_DIR / 'best_model.pkl'
SCALER_PATH = BASE_DIR / 'scaler.pkl'


def train_model():
    """Train the best ML model and write pickles."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Training dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    features = [
        'angle_of_incidence',
        'temperature_2_m_above_gnd',
        'wind_speed_10_m_above_gnd',
        'total_cloud_cover_sfc',
        'shortwave_radiation_backwards_sfc',
        'relative_humidity_2_m_above_gnd',
        'wind_direction_10_m_above_gnd',
        'mean_sea_level_pressure_MSL'
    ]
    X = df[features].values
    y = df["generated_power_kw"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            random_state=42
        )
    }

    best_score = -float('inf')
    best_model = None
    best_name = ""

    print("\nModel Results")
    print("=" * 40)

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        score = r2_score(y_test, pred)
        print(name, ":", round(score * 100, 2), "%")
        if score > best_score:
            best_score = score
            best_model = model
            best_name = name

    print("\nBest Model:", best_name)
    print("Accuracy:", round(best_score * 100, 2), "%")

    with MODEL_PATH.open('wb') as model_file:
        pickle.dump(best_model, model_file)

    with SCALER_PATH.open('wb') as scaler_file:
        pickle.dump(scaler, scaler_file)

    print("\nModel Saved")


if __name__ == '__main__':
    train_model()
