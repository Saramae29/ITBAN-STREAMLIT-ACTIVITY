import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.title("🦠 Global COVID-19 Statistics Dashboard")
st.write("Live data fetched from the public COVID-19 API (disease.sh).")

# API Request
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Create DataFrame
    df = pd.DataFrame(data)
    df = df[['country', 'cases', 'deaths', 'recovered', 'active', 'critical', 'todayCases']]
    df_sorted = df.sort_values(by='cases', ascending=False).head(10)

    st.subheader("Top 10 Countries by Total Cases")
    st.dataframe(df_sorted)

    # Chart 1: Bar Chart (matplotlib)
    st.subheader("📊 Total Cases (Bar Chart - Matplotlib)")
    fig, ax = plt.subplots()
    ax.bar(df_sorted['country'], df_sorted['cases'], color='orange')
    ax.set_ylabel("Total Cases")
    ax.set_title("Top 10 Countries by Cases")
    st.pyplot(fig)

    # Chart 2: Pie Chart (Plotly)
    st.subheader("🥧 Active Case Distribution (Pie Chart - Plotly)")
    fig2 = px.pie(df_sorted, names='country', values='active', title='Active Cases Distribution')
    st.plotly_chart(fig2)

    # Chart 3: Line Chart (Streamlit)
    st.subheader("📈 Cases Over Countries (Line Chart - Streamlit)")
    st.line_chart(df_sorted.set_index('country')[['cases', 'deaths']])

    # Chart 4: Area Chart (Streamlit)
    st.subheader("📉 Active vs Critical (Area Chart - Streamlit)")
    st.area_chart(df_sorted.set_index('country')[['active', 'critical']])

    # Chart 5: Heatmap (Seaborn)
    st.subheader("🔥 Correlation Heatmap (Seaborn)")
    corr = df_sorted[['cases', 'deaths', 'recovered', 'active', 'critical', 'todayCases']].corr()
    fig3, ax3 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='YlGnBu', ax=ax3)
    st.pyplot(fig3)

else:
    st.error("Failed to fetch data from the API.")
