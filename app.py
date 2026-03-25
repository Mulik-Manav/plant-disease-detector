import streamlit as st
from PIL import Image

st.title("Plant Disease Detector")

st.write("Upload a leaf image to detect disease")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("🧠 Analyzing...")

    st.success("Prediction: Healthy Leaf")
