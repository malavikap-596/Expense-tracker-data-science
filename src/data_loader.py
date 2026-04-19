import pandas as pd

def load_synthetic(path="data/synthetic_expenses.csv"):
    return pd.read_csv(path)

def load_real(path="data/real_expenses.csv"):
    try:
        df = pd.read_csv(path)
        print("✅ Real dataset loaded")
        return df
    except FileNotFoundError:
        print("⚠️ Real dataset not found, skipping...")
        return None