import pandas as pd

def category_analysis(df):
    result = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    return result

def monthly_analysis(df):
    df = df.copy()
    df['month'] = df['date'].dt.month_name()

    months_order = ['January','February','March','April','May','June',
                    'July','August','September','October','November','December']

    result = df.groupby('month')['amount'].sum().reindex(months_order)
    return result

def basic_stats(df):
    return {
        "avg": df['amount'].mean(),
        "max": df['amount'].max(),
        "min": df['amount'].min()
    }