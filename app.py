import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("model/model.h5")

# Class labels (EDIT based on your dataset)
class_names = ["Healthy", "Powdery Mildew", "Rust"]

st.title("🌿 Plant Disease Detector")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Prediction: {predicted_class}")
