import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/1.png")

with col2:
    st.title("Lyndon Tuala")
    content = """
    Hi!
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. \
         Feel free to cvontact me!")