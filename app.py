import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Data Analytics Dashboard")

np.random.seed(42)
num_rows = 100
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Books']
dates = pd.date_range(start="2023-01-01", periods=num_rows, freq='D')

data = {
    "Date": np.random.choice(dates, num_rows),
    "Category": np.random.choice(categories, num_rows),
    "Sales": np.random.randint(100, 2000, num_rows),
    "Revenue": np.random.randint(1000, 50000, num_rows),
    "Customer_Age": np.random.randint(18, 65, num_rows)
}

df = pd.DataFrame(data)

st.write("### Sample Data", df.head())

st.write("### 📈 Revenue Over Time")
df_sorted = df.sort_values("Date")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df_sorted["Date"], df_sorted["Revenue"], marker='o', linestyle='-')
ax.set_xlabel("Date")
ax.set_ylabel("Revenue ($)")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("### 📊 Sales Distribution by Category")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x="Category", y="Sales", data=df, ax=ax)
plt.xticks(rotation=30)
st.pyplot(fig)

st.write("### 🔥 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(6, 4))
numeric_df = df.select_dtypes(include=["number"]) 
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.write("### 👥 Customer Age Distribution")
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(df["Customer_Age"], bins=15, kde=True, ax=ax)
st.pyplot(fig)
