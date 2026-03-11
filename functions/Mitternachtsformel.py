import streamlit as st
import re
from datetime import datetime
import pytz

# -------- Streamlit App --------

st.title("Mitternachtsformel Rechner")

eingabe = st.text_input("Quadratische Formel eingeben (z.B. 2x^2+3x-5)")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Berechnen"):

    quadratische_Formel = parse_quadratic(eingabe)

    x1, x2, text = Mitternachtsformel(quadratische_Formel)

    result = {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
        "quadratische_Formel": quadratische_Formel,
        "Nullstelle1": x1,
        "Nullstelle2": x2,
        "Mitternachtsformel": text
    }

    st.session_state.history.append(result)

    st.write(result)


st.subheader("Berechnungsverlauf")

for r in st.session_state.history:
    st.write(r)