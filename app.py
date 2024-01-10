# Import Streamlit
import streamlit as st

# Create a text input box for the user to enter their name
name = st.text_input('Enter your name')

# When the user enters their name, print it
if name:
    st.write(f'Hello, {name}!')