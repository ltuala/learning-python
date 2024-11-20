import streamlit as st
import requests

api_key = "gqgjWn9TXw2HioJ3zMcvJd83cchfyGi2cJJY4epP"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


response = requests.get(url)
data = response.json()

st.title(data["title"])
st.image(data["hdurl"])
st.text(data["explanation"])
