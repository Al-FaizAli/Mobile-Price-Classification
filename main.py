import streamlit as st
st.title("My First Streamlit app")
st.write("Welcome to Streamlit App")
user_input=st.text_input("Enter Something...")
st.write(user_input)