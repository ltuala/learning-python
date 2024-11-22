import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", 
                        ("Temperature", "Sky"))
                    
st.subheader(f"{option} for the next {days} days in {place.title()}")

if place:
    try:
        data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in data]
            dates = [dict["dt_txt"] for dict in data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png",
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in data]
            dates = [dict["dt_txt"] for dict in data]
            image_paths = [images[condition] for condition in sky_conditions]

            columns_per_row = 8
            cols = st.columns(columns_per_row)
            for i, path in enumerate(image_paths):
                with cols[i % columns_per_row]:
                    st.caption(f"{dates[i]}")
                    st.image(path, width=115, caption=f"{sky_conditions[i]}")
    except KeyError:
        st.info("That place does not exist.")
