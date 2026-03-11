import streamlit as st
import pandas as pd
import joblib
from feature_eng import get_stay_category, get_booking_window, get_season


import streamlit as st
import pandas as pd
import joblib
from feature_eng import get_stay_category, get_booking_window, get_season


def build_features(listing, nights, lead_time, month, weekday, monthly_demand_map):

    monthly_demand = monthly_demand_map.get(month, 0)

    is_weekend = weekday in ["Friday","Saturday","Sunday"]

    stay_category = get_stay_category(nights)

    booking_window = get_booking_window(lead_time)

    season = get_season(month)

    input_data = pd.DataFrame({
        'listing':[listing],
        'nights':[nights],
        'month':[month],
        'monthly_demand':[monthly_demand],
        'weekday':[weekday],
        'is_weekend':[is_weekend],
        'stay_category':[stay_category],
        'booking_window':[booking_window],
        'season':[season]
    })

    return input_data

# load trained model
model = joblib.load("pricing_model.pkl")

# monthly demand map (computed from dataset)
monthly_demand_map = joblib.load("monthly_demand_map.pkl")



st.title("Airbnb Dynamic Pricing Engine")

st.write("Enter booking details to get a recommended nightly price")

# Inputs
listing = st.selectbox(
    "Listing",
    ["Room 1","Room 2","Room 3","Room 4","Room 5","Room 6","Room 7","Room 8","Room 9","Room 10","Room 11","Room 12"]
)

nights = st.slider("Number of nights", 1, 14)

lead_time = st.slider("Lead time (days before booking)", 0, 120)

month = st.selectbox(
    "Month",
    list(range(1,13))
)

weekday = st.selectbox(
    "Check-in weekday",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
)


# Predict button
if st.button("Predict Price"):

    input_data = build_features(
        listing,
        nights,
        lead_time,
        month,
        weekday,
        monthly_demand_map
    )

    price = model.predict(input_data)[0]

    st.success(f"Recommended price: €{round(price,2)} per night")