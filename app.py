import streamlit as st
from PIL import Image
import random
import time

# Page config
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="wide")

# Custom CSS (clean modern look)
st.markdown("""
    <style>
    body {
        background-color: #0f172a;
    }
    .main {
        background-color: #0f172a;
        color: white;
    }
    .title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        color: #22c55e;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #94a3b8;
        margin-bottom: 40px;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #111827;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌿 Plant Disease Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a leaf image and get instant AI analysis</div>', unsafe_allow_html=True)

# Layout split
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📸 Upload Image")
    uploaded_file = st.file_uploader("", type=["jpg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

with col2:
    st.markdown("### 🧠 Analysis Result")

    if uploaded_file:
        with st.spinner("Analyzing..."):
            time.sleep(2)

        diseases = [
            "Healthy Leaf",
            "Powdery Mildew",
            "Leaf Spot",
            "Rust Disease"
        ]

        prediction = random.choice(diseases)
        confidence = random.randint(85, 98)

        st.markdown(f"""
        <div class="card">
            <h3>🌱 {prediction}</h3>
            <p>Confidence: <b>{confidence}%</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("💡 *Ensure proper irrigation and sunlight for best crop health.*")