import pandas as pd
import streamlit as st
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
from functions.Mitternachtsformel import Mitternachtsformel, parse_quadratic
st.title("Mitternachtsformel berechnen")

st.write("Die Mitternachtsformel, auch bekannt als die quadratische Lösungsformel, ist eine Methode zur Berechnung der Lösungen einer quadratischen Gleichung der Form ax^2 + bx + c = 0. Die Formel lautet: x = (-b ± √(b^2 - 4ac)) / (2a).")

st.write("Hier kannst du die Mitternachtsformel anwenden, um die Lösungen einer quadratischen Gleichung zu berechnen.")

with st.form(key='my_form'): 
    input_string = st.text_input("Gib die quadratische Gleichung ein (z.B. 2x^2 + 3x - 5):")
    submitted = st.form_submit_button("Berechnen")

if submitted:
    quadratische_Formel = parse_quadratic(input_string)
    x1, x2, text = Mitternachtsformel(quadratische_Formel)

    st.write(x1, x2)


# --- NEW CODE to update history in session state and display it ---
    st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])])
        
# --- NEW CODE to display the history table ---
st.dataframe(st.session_state['data_df'])