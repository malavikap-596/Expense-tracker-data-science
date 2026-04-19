import pandas as pd

def clean_data(df):
    df = df.copy()

    # 🔹 Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    print("Columns after cleaning:", df.columns.tolist())  # DEBUG

    # 🔹 Handle alternate names
    rename_map = {
        'date': 'date',
        'transaction_date': 'date',
        'day': 'date',

        'category': 'category',
        'type': 'category',

        'amount': 'amount',
        'amt': 'amount'
    }

    df = df.rename(columns=rename_map)

    # 🔹 FINAL CHECK (IMPORTANT)
    required = ['date', 'category', 'amount']
    for col in required:
        if col not in df.columns:
            raise ValueError(f"❌ Missing required column: {col}")

    # 🔹 Convert types
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # 🔹 Drop invalid rows
    df = df.dropna(subset=['date', 'amount'])

    return df