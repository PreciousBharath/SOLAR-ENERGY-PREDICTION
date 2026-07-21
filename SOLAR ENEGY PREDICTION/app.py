import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load model and scaler
# -----------------------------

model = pickle.load(open("best_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# -----------------------------
# Page settings
# -----------------------------

st.set_page_config(
    page_title="Solar Power Prediction",
    page_icon="☀",
    layout="wide"
)

# -----------------------------
# Background + UI styling
# -----------------------------

st.markdown(
"""
<style>

.stApp{
background-image:url("https://images.unsplash.com/photo-1509391366360-2e959784a276?q=80&w=1920");
background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;
}

.main{
background-color:rgba(0,0,0,0.55);
padding:20px;
border-radius:15px;
}

h1{
color:white;
text-align:center;
font-size:45px;
}

h3{
color:white;
}

label{
color:white !important;
font-size:16px !important;
font-weight:bold !important;
}

div[data-baseweb="select"]{
background-color:white;
border-radius:10px;
}

.stButton>button{
width:100%;
height:60px;
font-size:22px;
border-radius:15px;
font-weight:bold;
}

.result{
background:white;
padding:20px;
border-radius:15px;
font-size:30px;
text-align:center;
font-weight:bold;
}

</style>
""",
unsafe_allow_html=True
)

# -----------------------------
# Title
# -----------------------------

st.markdown(
"""
<h1>☀ Solar Power Prediction System</h1>
""",
unsafe_allow_html=True
)

st.write("")

# -----------------------------
# Dropdown values
# -----------------------------

temperature = list(range(-10,51,5))

humidity = list(range(0,101,5))

pressure = list(range(980,1051,5))

precipitation = list(range(0,101,5))

snowfall = list(range(0,51,2))

cloud = list(range(0,101,10))

radiation = list(range(0,1001,50))

wind = list(range(0,51,2))

direction = list(range(0,361,10))

angle = list(range(0,361,5))

# -----------------------------
# Layout
# -----------------------------

col1,col2,col3=st.columns(3)

with col1:

    st.subheader("Weather Data")

    temp=st.selectbox(
    "Temperature (°C)",
    temperature
    )

    humidity1=st.selectbox(
    "Humidity (%)",
    humidity
    )

    pressure1=st.selectbox(
    "Pressure",
    pressure
    )

    precipitation1=st.selectbox(
    "Precipitation",
    precipitation
    )

    snowfall1=st.selectbox(
    "Snowfall",
    snowfall
    )

    cloud1=st.selectbox(
    "Cloud Cover",
    cloud
    )

    high_cloud=st.selectbox(
    "High Cloud Cover",
    cloud
    )


with col2:

    st.subheader("Cloud & Wind Data")

    medium_cloud=st.selectbox(
    "Medium Cloud Cover",
    cloud
    )

    low_cloud=st.selectbox(
    "Low Cloud Cover",
    cloud
    )

    radiation1=st.selectbox(
    "Shortwave Radiation",
    radiation
    )

    wind10=st.selectbox(
    "Wind Speed 10m",
    wind
    )

    direction10=st.selectbox(
    "Wind Direction 10m",
    direction
    )

    wind80=st.selectbox(
    "Wind Speed 80m",
    wind
    )

    direction80=st.selectbox(
    "Wind Direction 80m",
    direction
    )


with col3:

    st.subheader("Solar Angle Data")

    wind900=st.selectbox(
    "Wind Speed 900mb",
    wind
    )

    direction900=st.selectbox(
    "Wind Direction 900mb",
    direction
    )

    gust=st.selectbox(
    "Wind Gust",
    wind
    )

    incidence=st.selectbox(
    "Angle Of Incidence",
    angle
    )

    zenith=st.selectbox(
    "Zenith",
    angle
    )

    azimuth=st.selectbox(
    "Azimuth",
    angle
    )

st.write("")
st.write("")

# -----------------------------
# Prediction button
# -----------------------------

if st.button("Predict Solar Power"):

    values=np.array([[
        temp,
        humidity1,
        pressure1,
        precipitation1,
        snowfall1,
        cloud1,
        high_cloud,
        medium_cloud,
        low_cloud,
        radiation1,
        wind10,
        direction10,
        wind80,
        direction80,
        wind900,
        direction900,
        gust,
        incidence,
        zenith,
        azimuth
    ]])

    scaled=scaler.transform(values)

    prediction=model.predict(scaled)

    st.markdown(
    f"""
    <div class="result">
    ☀ Predicted Solar Power
    <br><br>
    {round(prediction[0],2)} kW
    </div>
    """,
    unsafe_allow_html=True
    )