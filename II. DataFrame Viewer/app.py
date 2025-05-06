import streamlit as st
import pandas as pd

st.title("📊 DataFrame Viewer")
st.write("Upload a CSV file to explore and filter your data.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data with pandas
    df = pd.read_csv(uploaded_file)

    # Ensure the file has at least 5 columns
    if df.shape[1] < 5:
        st.warning("The uploaded file must have at least 5 columns.")
    else:
        # Checkbox to show raw data
        if st.checkbox("Show raw data"):
            st.subheader("Raw Data")
            st.dataframe(df)

        # Selectbox to filter by a column
        column = st.selectbox("Select a column to filter:", df.columns)

        # Get unique values and let user filter
        unique_vals = df[column].unique()
        selected_val = st.selectbox(f"Select a value from '{column}':", unique_vals)

        # Show filtered data
        filtered_df = df[df[column] == selected_val]
        st.subheader("Filtered Data")
        st.dataframe(filtered_df)
else:
    st.info("Please upload a CSV file.")
