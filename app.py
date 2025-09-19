import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# App title
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers from the CORD-19 dataset.")

# Filter years
year_range = st.slider("Select year range", 2015, 2025, (2019, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.write(filtered[['title','authors','journal','year']].head())

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# Top journals visualization 
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)
