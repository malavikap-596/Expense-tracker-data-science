import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/raw_expenses.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.title("💸 Expense Tracker Dashboard")

# Total spending
total = df['Amount'].sum()
st.metric("Total Spending", f"₹{total}")

# Category chart
cat = df.groupby('Category')['Amount'].sum().reset_index()

fig1 = px.pie(cat, values='Amount', names='Category', title="Category Distribution")
st.plotly_chart(fig1)

# Monthly trend
df['Month'] = df['Date'].dt.month_name()
month = df.groupby('Month')['Amount'].sum().reset_index()

fig2 = px.bar(month, x='Month', y='Amount', title="Monthly Spending")
st.plotly_chart(fig2)

st.success("Dashboard Loaded Successfully!")