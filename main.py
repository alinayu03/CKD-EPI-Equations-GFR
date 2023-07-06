import streamlit as st
import numpy as np

st.title("CKD-EPI GFR Calculator")


def calculate_gfr(age, gender, race, scr):
    """
    Calculate GFR using CKD-EPI equation
    """
    scr = scr / 0.9 if scr <= 0.9 else (scr / 0.9)**-1.209
    age_factor = 0.993**age
    gender_factor = 0.739 if gender == "female" else 1
    race_factor = 1.159 if race == "black" else 1
    return 141 * min(scr, 1)**-0.329 * max(scr, 1)**-1.209 * age_factor * gender_factor * race_factor


age = st.number_input('Insert your age', min_value=1, max_value=120, value=50)
gender = st.radio("Select your gender", ("male", "female"))
race = st.radio("Select your race", ("black", "other"))
scr = st.number_input('Insert your Serum Creatinine (mg/dL)',
                      min_value=0.1, max_value=10.0, value=1.0)

if st.button('Calculate GFR'):
    gfr = calculate_gfr(age, gender, race, scr)
    st.write(
        f'Your estimated Glomerular Filtration Rate (GFR) is {gfr:.2f} mL/min/1.73 m^2')
