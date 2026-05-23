import streamlit as st
import requests

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌾",
    layout="wide"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton>button {
    width: 100%;
    background-color: #2e8b57;
    color: white;
    height: 3em;
    border-radius: 10px;
    font-size: 18px;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER
# ======================================

st.title("🌾 Smart Agriculture AI Platform")
st.markdown("AI-powered crop intelligence and yield prediction system")

st.divider()

# ======================================
# SIDEBAR
# ======================================

st.sidebar.header("📋 Input Parameters")

year = st.sidebar.number_input(
    "Year",
    min_value=1990,
    max_value=2035,
    value=2024
)

area = st.sidebar.selectbox(
    "Country",
    [
        "India",
        "USA",
        "Brazil",
        "China",
        "Australia",
        "Nigeria",
        "Argentina"
    ]
)

pesticides = st.sidebar.number_input(
    "Pesticides Tonnes",
    min_value=0,
    max_value=1000,
    value=200
)

# ======================================
# MAIN BUTTON
# ======================================

if st.sidebar.button("🚀 Run Smart Prediction"):

    payload = {
        "Year": year,
        "Area": area,
        "pesticides_tonnes": pesticides
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/smart-predict",
            json=payload
        )

        result = response.json()

        # ======================================
        # TOP METRICS
        # ======================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🌡 Temperature",
                f"{result['weather']['temperature']} °C"
            )

        with col2:
            st.metric(
                "🌧 Rainfall",
                f"{result['weather']['rainfall']} mm"
            )

        with col3:
            st.metric(
                "🌱 Recommended Crop",
                result['recommended_crop']
            )

        with col4:
            st.metric(
                "📈 Predicted Yield",
                round(result['predicted_yield'], 2)
            )

        st.divider()

        # ======================================
        # MAIN CONTENT
        # ======================================

        left, right = st.columns([2,1])

        with left:

            st.subheader("🧠 AI Agricultural Insights")

            st.success(
                f"""
                Recommended Crop: {result['recommended_crop']}
                
                Fertilizer Suggestion:
                {result['fertilizer']}
                """
            )

            st.info(
                f"""
                Based on real-time weather conditions in {area},
                the AI system predicts a yield of
                {round(result['predicted_yield'], 2)} hg/ha.
                """
            )

        with right:

            st.subheader("🌍 Weather Summary")

            st.write(f"📍 Location: {area}")
            st.write(f"🌡 Temperature: {result['weather']['temperature']} °C")
            st.write(f"🌧 Rainfall: {result['weather']['rainfall']} mm")

        st.divider()

        # ======================================
        # EXTRA ANALYTICS
        # ======================================

        st.subheader("📊 System Intelligence")

        st.progress(85)

        st.caption(
            "AI confidence score based on weather, crop recommendation, and yield estimation."
        )

    except Exception as e:

        st.error(f"Error: {str(e)}")

else:

    st.info("👈 Enter parameters from sidebar and click Run Smart Prediction")