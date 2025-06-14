import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Kypraios Kyriakos")
    content = """
    Hi, I am Kypraios Kyriakos, a backend software engineer with a passion for programming.
    I live in Athens, Greece and I am currently working as a software engineer at a company that specializes in web applications.
    I have a strong background in Python and C#, and I am always eager to learn new technologies and improve my skills.
    I have experience in building web applications using Python and C#, and I am familiar with various frameworks such as Django, Flask, and ASP.NET.
    I am also experienced in building RESTful APIs and working with databases such as MySQL, PostgreSQL, and MongoDB.
    I have a strong understanding of software development principles and best practices, and I am always looking for ways to improve my code and make it more efficient.
    """
    st.info(content)

content2 = """
Below you can find some of my demo applications I have built in Python. Feel free to contact me.
"""
st.write(content2)

# Create a list of demo applications
col3,empty_column ,col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source] ({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source] ({row['url']})")