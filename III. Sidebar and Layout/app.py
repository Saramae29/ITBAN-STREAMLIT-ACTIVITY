import streamlit as st

st.title("🏢 Data Warehousing & Enterprise Data Management")
st.write("This app demonstrates how to use Streamlit layout features with data management content.")

# Sidebar for filters and options
st.sidebar.header("🔧 Filters & Options")
topic = st.sidebar.selectbox("Choose a Topic", ["Data Warehousing", "ETL Process", "Enterprise Data Management"])

show_summary = st.sidebar.checkbox("Show Summary", value=True)

# Use tabs to organize main content
tab1, tab2 = st.tabs(["📘 Overview", "📊 Detailed Insights"])

with tab1:
    st.subheader("Overview")
    if topic == "Data Warehousing":
        st.write("A **Data Warehouse** is a central repository for integrated data from various sources, structured for query and analysis.")
    elif topic == "ETL Process":
        st.write("**ETL (Extract, Transform, Load)** is a process that extracts data from sources, transforms it for analysis, and loads it into a data warehouse.")
    elif topic == "Enterprise Data Management":
        st.write("**Enterprise Data Management (EDM)** is the capability of an organization to govern, integrate, and secure data for effective decision-making.")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("📦 Storage Architecture"):
            st.write("Data Warehouses use star or snowflake schemas, optimized for analytical querying and reporting.")

    with col2:
        with st.expander("🔄 Data Integration"):
            st.write("Data is integrated using ETL/ELT pipelines, often orchestrated with tools like Apache Airflow or Informatica.")

if show_summary:
    st.info("Use the sidebar to explore topics. Tabs and expanders help you navigate and understand key concepts in data warehousing and EDM.")
