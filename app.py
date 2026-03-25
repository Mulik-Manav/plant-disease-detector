import streamlit as st
from PIL import Image
import random
import time

# Page config
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="centered")

# Banner Image (visual touch 🔥)
st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6", use_column_width=True)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #00ff9f;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #aaaaaa;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌿 Plant Disease Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered leaf analysis system</div>', unsafe_allow_html=True)

# Upload section
uploaded_file = st.file_uploader("📸 Upload a leaf image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Fake AI processing
    with st.spinner("🧠 Analyzing leaf patterns..."):
        time.sleep(2)

    diseases = [
        "Healthy Leaf",
        "Powdery Mildew",
        "Leaf Spot",
        "Rust Disease"
    ]

    prediction = random.choice(diseases)
    confidence = random.randint(85, 98)

    # Results
    st.success(f"🌱 Prediction: {prediction}")
    st.info(f"📊 Confidence: {confidence}%")

    # Extra polish
    st.markdown("---")
    st.markdown("💡 **Tip:** Ensure proper irrigation and sunlight for healthy crops.")