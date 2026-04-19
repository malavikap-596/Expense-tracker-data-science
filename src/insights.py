def generate_insights(df, category_data, monthly_data):
    insights = []

    top_category = category_data.idxmax()
    top_value = category_data.max()

    insights.append(f"Highest spending category: {top_category} (₹{top_value})")

    # Monthly trend
    trend = monthly_data.diff()

    if trend.iloc[-1] > 0:
        insights.append("Spending increased in the last month 📈")
    else:
        insights.append("Spending decreased in the last month 📉")

    # High spending alert
    if top_value > 0.3 * df['amount'].sum():
        insights.append(f"⚠️ High spending detected in {top_category}")

    return insights