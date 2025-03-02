import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\profile.jpeg", width=450)

with col2:
    st.title("B R Balaharish")
    description = """ Hi, I am Balaharish. I am a Python programmer.
    I graduated from Raffles Institution in 2024.
    """
    st.info(description)

st.write("Below you can find some apps that I have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")