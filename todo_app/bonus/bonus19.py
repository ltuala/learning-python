import streamlit as st
from PIL import Image

def convert_image(image):
    # Create a pillow image instance
    img = Image.open(image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    return gray_img

st.subheader("Color to Grayscale Converter")

with st.expander("Upload an image"):
    # Start the camera
    uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    gray_camera_img = convert_image(camera_image)

    # Render the grayscale image on the webpage
    st.image(gray_camera_img)

if uploaded_image:
    # Create a pillow image instance
    gray_uploaded_img = convert_image(uploaded_image)

    # Render the grayscale image on the webpage
    st.image(gray_uploaded_img)  
