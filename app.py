# Python
import streamlit as st

def main():
    st.title('Hello App')
    name = st.text_input('Enter your name')
    if st.button('Submit'):
        st.write(f'Hello, {name}!')

if __name__ == "__main__":
    main()