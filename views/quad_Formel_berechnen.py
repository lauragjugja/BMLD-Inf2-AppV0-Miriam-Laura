import pandas as pd

import streamlit as st

import numpy as np

import matplotlib.pyplot as plt
 
from utils.data_manager import DataManager

from functions.Mitternachtsformel import Mitternachtsformel, parse_quadratic
 
# WICHTIG: session_state initialisieren

if "data_df" not in st.session_state:

    st.session_state["data_df"] = pd.DataFrame(

        columns=["formel", "x1", "x2", "beschreibung"]

    )
 
st.title("Mitternachtsformel berechnen")
 
st.write("Die Mitternachtsformel, auch bekannt als die quadratische Lösungsformel, ist eine Methode zur Berechnung der Lösungen einer quadratischen Gleichung der Form ax^2 + bx + c = 0.")
 
st.write("Hier kannst du die Mitternachtsformel anwenden, um die Lösungen einer quadratischen Gleichung zu berechnen.")
 
with st.form(key='my_form'):

    input_string = st.text_input("Gib die quadratische Gleichung ein (z.B. 2x^2 + 3x - 5):")

    submitted = st.form_submit_button("Berechnen")
 
if submitted:

    quadratische_Formel = parse_quadratic(input_string)

    x1, x2, text = Mitternachtsformel(quadratische_Formel)
 
    st.write(x1, x2)
 
    result = {

        "formel": input_string,

        "x1": x1,

        "x2": x2,

        "beschreibung": text

    }
 
    st.session_state['data_df'] = pd.concat(

        [st.session_state['data_df'], pd.DataFrame([result])],

        ignore_index=True

    )
 
    st.subheader("Grafische Darstellung deiner neusten Eingabe")
 
    a, b, c = quadratische_Formel
 
    if a != 0:

        x_min = min(x1 or 0, x2 or 0) - 5 if (x1 is not None and x2 is not None) else -10

        x_max = max(x1 or 0, x2 or 0) + 5 if (x1 is not None and x2 is not None) else 10
 
        x_vals = np.linspace(x_min, x_max, 300)

        y_vals = a * x_vals**2 + b * x_vals + c
 
        fig, ax = plt.subplots(figsize=(10, 6))
 
        ax.plot(x_vals, y_vals, linewidth=2)
 
        ax.axhline(y=0)

        ax.axvline(x=0)
 
        if x1 is not None and x2 is not None:

            ax.plot([x1, x2], [0, 0], 'o')

        elif x1 is not None:

            ax.plot([x1], [0], 'o')
 
        st.pyplot(fig)
 
# Verlauf anzeigen

if not st.session_state["data_df"].empty:

    st.subheader("Berechnungsverlauf")

    st.dataframe(st.session_state['data_df'])
 