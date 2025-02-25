import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\profile.jpeg", width=450)

with col2:
    st.title("B R Balaharish")
    description = """ Hi, I am Balaharish, I am a Python programmer.
    I graduated from Raffles Institution in 2024.
    """
    st.info(description)