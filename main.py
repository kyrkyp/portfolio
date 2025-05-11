import streamlit as st

# Set the page configuration
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Kypraios Kyriakos")
    content = """
    I am a software engineer with a passion for creating innovative solutions to complex problems.
    I love coding and I have a deep understanding of software development principles.
    I am always eager to learn new technologies and improve my skills.
    I am a team player and enjoy collaborating with others to achieve common goals.
    I am currently seeking new opportunities to apply my skills and contribute to exciting projects.
    """
    st.info(content)