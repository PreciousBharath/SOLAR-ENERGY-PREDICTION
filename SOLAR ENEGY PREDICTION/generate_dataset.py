import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_CSV = BASE_DIR / 'spg.csv'
OUTPUT_CSV = BASE_DIR / 'solar_dataset.csv'

FEATURES = [
    'angle_of_incidence',
    'temperature_2_m_above_gnd',
    'wind_speed_10_m_above_gnd',
    'total_cloud_cover_sfc',
    'shortwave_radiation_backwards_sfc',
    'relative_humidity_2_m_above_gnd',
    'wind_direction_10_m_above_gnd',
    'mean_sea_level_pressure_MSL',
    'generated_power_kw'
]

if not INPUT_CSV.exists():
    raise FileNotFoundError(f"Training dataset not found: {INPUT_CSV}")

df = pd.read_csv(INPUT_CSV)
missing = [c for c in FEATURES if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns in dataset: {missing}")

subset = df[FEATURES]
subset.to_csv(OUTPUT_CSV, index=False)
print(f"Created {OUTPUT_CSV.name} with {len(subset)} rows and {len(subset.columns)} columns")
