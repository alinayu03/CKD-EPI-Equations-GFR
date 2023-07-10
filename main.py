import streamlit as st

def calculate_2021gfr(scr, age, sex):
    # 2021 CKD-EPI creatinine equation for GFR
    if sex == 'Male':
        if scr <= 0.9:
            A = 0.9
            B = -0.302
        else:
            A = 0.9
            B = -1.2
        gfr = 142 * (scr/A)**B * 0.9938**age
    elif sex == 'Female':
        if scr <= 0.7:
            A = 0.7
            B = -0.241
        else:
            A = 0.7
            B = -0.241
        gfr = 142 * (scr/A)**B * 0.9938**age * 1.012
    return gfr

def calculate_2021gfrC(scr, scys, age, sex):
    # 2021 CKD-EPI creatinine-crystatin C equation for GFR
    if sex == 'Male':
        if scr <= 0.9:
            if scys <= 0.8:
                A = 0.9
                B = -0.144
                C = 0.8
                D = -0.323
            elif scys > 0.8:
                A = 0.9
                B = -0.144
                C = 0.8
                D = -0.778
        elif scr > 0.9: 
            if scys <= 0.8:
                A = 0.9
                B = -0.544
                C = 0.8
                D = -0.323
            elif scys > 0.8:
                A = 0.9
                B = -0.544
                C = 0.8
                D = -0.778
        gfr = 135 * (scr/A)**B * (scys/C)**D * 0.9961**age
    elif sex == 'Female':
        if scr <= 0.7:
            if scys <= 0.8:
                A = 0.7
                B = -0.219
                C = 0.8
                D = -0.323
            elif scys > 0.8:
                A = 0.7
                B = -0.219
                C = 0.8
                D = -0.778
        elif scr > 0.7:
            if scys <= 0.8:
                A = 0.7
                B = -0.544
                C = 0.8
                D = -0.323
            elif scys > 0.8:
                A = 0.7
                B = -0.544
                C = 0.8
                D = -0.778
        gfr = 135 * (scr/A)**B * (scys/C)**D * 0.9961**age * 0.963
    return gfr

# Streamlit app
st.title('2021 CKD-EPI Creatinine Equations for Glomerular Filtration Rate')
st.sidebar.title("Equation")
equation = st.sidebar.radio("Select an Equation",
                            ("2021 CKD-EPI Creatinine",
                            "2021 CKD-EPI Creatinine-Crystatin C"))

scr = st.number_input(
    'Enter your Serum creatinine (mg/dL)', min_value=0.0, max_value=20.0, step=0.1)
age = st.number_input('Enter your Age (years)', min_value=1, max_value=120, step=1)
sex = st.selectbox('Select your Sex', options=['Male', 'Female'])

if equation == "2021 CKD-EPI Creatinine-Crystatin C":
    scys = st.number_input(
        'Enter your Serum cystatin C (mg/L)', min_value=0.0, max_value=20.0, step=0.1)

if st.button('Calculate Glomerular Filtration Rate'):
    if equation == "2021 CKD-EPI Creatinine":
        gfr = calculate_2021gfr(scr, age, sex)
    elif equation == "2021 CKD-EPI Creatinine-Crystatin C":
        gfr = calculate_2021gfrC(scr, scys, age, sex)
    st.write(f'Your GFR is {gfr:.2f} mL/min/1.73m².')
