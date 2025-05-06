import streamlit as st

# Title and Headers
st.title("👋 Hello, Streamlit!")
st.header("🎯 Streamlit Basics Demo")
st.write("Welcome! This app demonstrates the basic features of a Streamlit app.")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Display output based on user input
if name:
    st.write(f"👋 Hello, **{name}**! You are {age} years old.")
    if age < 18:
        st.write("You're a minor.")
    elif age < 65:
        st.write("You're an adult.")
    else:
        st.write("You're a senior citizen.")
