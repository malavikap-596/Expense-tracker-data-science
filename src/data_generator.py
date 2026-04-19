import pandas as pd
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from src.config import RANDOM_SEED, DEFAULT_ROWS

np.random.seed(RANDOM_SEED)

# ----------------------------------------
# 💰 Category-wise realistic spending
# ----------------------------------------
def get_amount(category, is_weekend):
    if category == "Food":
        return np.random.randint(200, 1000) if is_weekend else np.random.randint(100, 500)
    
    elif category == "Travel":
        return np.random.randint(500, 3000)
    
    elif category == "Shopping":
        return np.random.randint(1000, 5000) if is_weekend else np.random.randint(500, 3000)
    
    elif category == "Bills":
        return np.random.randint(1000, 4000)
    
    elif category == "Entertainment":
        return np.random.randint(300, 2000) if is_weekend else np.random.randint(200, 1000)
    
    elif category == "Health":
        return np.random.randint(200, 2500)
    
    return np.random.randint(100, 2000)


# ----------------------------------------
# 💳 Payment method bias
# ----------------------------------------
def get_payment_method():
    return np.random.choice(
        ["UPI", "Card", "Cash"],
        p=[0.5, 0.3, 0.2]   # UPI most common (realistic for India)
    )


# ----------------------------------------
# 📊 Main Data Generator
# ----------------------------------------
def generate_data(n=DEFAULT_ROWS, save_path="data/synthetic_expenses.csv"):
    
    categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Health"]

    start_date = datetime(2025, 1, 1)

    records = []

    for i in range(n):
        date = start_date + timedelta(days=np.random.randint(0, 365))
        category = np.random.choice(categories)

        is_weekend = date.weekday() >= 5

        amount = get_amount(category, is_weekend)
        payment = get_payment_method()

        records.append({
            "date": date,
            "category": category,
            "amount": amount,
            "payment_method": payment
        })

    df = pd.DataFrame(records)

    # Save dataset
    df.to_csv(save_path, index=False)

    print(f"✅ Synthetic dataset generated with {n} records")
    
    return df