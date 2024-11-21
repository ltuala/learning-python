import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")
x = st.selectbox("Select the data for the X-axis", 
                    options=("GDP", "Happiness", "Generosity"))
y = st.selectbox("Select the data for the Y-axis", 
                    options=("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")
x_data = df[x.lower()]
y_data = df[y.lower()]

st.subheader(f"{x} and {y}")
figure = px.scatter(x=x_data, y=y_data, labels={"x": x, "y": y})
st.plotly_chart(figure)