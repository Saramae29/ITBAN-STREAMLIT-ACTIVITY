import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Replace with your actual database credentials
DB_USER = "root1"
DB_PASS = "password"
DB_HOST = "localhost"
DB_NAME = "sample_db"

# Optional simple authentication
st.title("🔐 User Login (Demo Auth)")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
auth_button = st.button("Login")

# Very basic hardcoded user check (for demo purposes only)
if username == "admin" and password == "1234":
    st.success("Logged in successfully!")

    # Connect to database
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

    # Query section
    st.header("📋 View and Filter Data")
    with engine.connect() as conn:
        query = "SELECT * FROM employees"
        df = pd.read_sql(query, conn)

        # Filter by department
        dept = st.selectbox("Filter by Department", df["department"].unique())
        filtered_df = df[df["department"] == dept]
        st.dataframe(filtered_df)

    # Form to insert new employee
    st.header("➕ Add New Employee")
    with st.form("insert_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=18, max_value=100)
        department = st.text_input("Department")
        submitted = st.form_submit_button("Insert")

        if submitted:
            insert_query = text("INSERT INTO employees (name, age, department) VALUES (:name, :age, :dept)")
            with engine.begin() as conn:
                conn.execute(insert_query, {"name": name, "age": age, "dept": department})
            st.success(f"Employee {name} added successfully!")

else:
    if auth_button:
        st.error("Invalid credentials. Try 'admin' / '1234' for demo.")
