# ============================================
# 💸 EXPENSE TRACKER - MAIN EXECUTION FILE
# ============================================

import os

from src.data_generator import generate_data
from src.data_cleaning import clean_data
from src.analysis import category_analysis, monthly_analysis, basic_stats
from src.visualization import plot_charts
from src.insights import generate_insights

# --------------------------------------------
# 1️⃣ Ensure required folders exist
# --------------------------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# --------------------------------------------
# 2️⃣ Generate Synthetic Data
# --------------------------------------------
print("🔄 Generating synthetic dataset...")
df = generate_data(n=500, save_path="data/synthetic_expenses.csv")

# --------------------------------------------
# 3️⃣ Clean Data
# --------------------------------------------
print("🧹 Cleaning data...")
df = clean_data(df)

print("\n📊 Using: Synthetic Dataset")

# --------------------------------------------
# 4️⃣ Perform Analysis
# --------------------------------------------
print("📊 Performing analysis...")

category_data = category_analysis(df)
monthly_data = monthly_analysis(df)
stats = basic_stats(df)

# --------------------------------------------
# 5️⃣ Save Outputs
# --------------------------------------------
print("💾 Saving outputs...")

category_data.to_csv("outputs/category_summary.csv")
monthly_data.to_csv("outputs/monthly_summary.csv")
df.to_csv("outputs/cleaned_data.csv", index=False)

# --------------------------------------------
# 6️⃣ Visualization
# --------------------------------------------
print("📈 Generating charts...")
plot_charts(category_data, monthly_data)

# --------------------------------------------
# 7️⃣ Insights
# --------------------------------------------
print("💡 Generating insights...")

insights = generate_insights(df, category_data, monthly_data)

# --------------------------------------------
# 8️⃣ Display Results
# --------------------------------------------
print("\n==============================")
print("📊 SUMMARY STATISTICS")
print("==============================")
print(f"Average Spend: ₹{stats['avg']:.2f}")
print(f"Max Spend: ₹{stats['max']}")
print(f"Min Spend: ₹{stats['min']}")

print("\n==============================")
print("💡 INSIGHTS")
print("==============================")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")

print("\n✅ Project Execution Completed Successfully!")