import matplotlib.pyplot as plt

def plot_charts(category_data, monthly_data):
    plt.figure(figsize=(12,5))

    # Pie chart
    plt.subplot(1,2,1)
    category_data.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Category Distribution")

    # Bar chart
    plt.subplot(1,2,2)
    monthly_data.plot(kind='bar')
    plt.title("Monthly Spending")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("images/charts.png")
    plt.show()