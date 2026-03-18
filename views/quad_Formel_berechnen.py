import streamlit as st
from functions.Mitternachtsformel import Mitternachtsformel, parse_quadratic
st.title("Mitternachtsformel berechnen")

st.write("Die Mitternachtsformel, auch bekannt als die quadratische Lösungsformel, ist eine Methode zur Berechnung der Lösungen einer quadratischen Gleichung der Form ax^2 + bx + c = 0. Die Formel lautet: x = (-b ± √(b^2 - 4ac)) / (2a).")

st.write("Hier kannst du die Mitternachtsformel anwenden, um die Lösungen einer quadratischen Gleichung zu berechnen.")

input_string = st.text_input("Gib die quadratische Gleichung ein (z.B. 2x^2 + 3x - 5):")

if input_string:
    quadratische_Formel = parse_quadratic(input_string)
    result = Mitternachtsformel(quadratische_Formel)
    st.write("Das Ergebnis ist:", result)

 # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

import csv

class DataManager:
    """Einfacher DataManager zum Speichern von DataFrame / Liste/Dict als CSV."""

    def save_user_data(self, data, filename='data.csv'):
        try:
            import pandas as pd
        except Exception:
            pd = None

        # pandas.DataFrame -> to_csv
        if pd is not None and hasattr(data, "to_csv"):
            data.to_csv(filename, index=False)
            return

        # Liste von Dicts
        if isinstance(data, list) and data and isinstance(data[0], dict):
            keys = data[0].keys()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, keys)
                writer.writeheader()
                writer.writerows(data)
            return

        # Einzelnes Dict
        if isinstance(data, dict):
            keys = data.keys()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, keys)
                writer.writeheader()
                writer.writerow(data)
            return

        # Fallback: String schreiben
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(data))

# --- NEW CODE to display the history table ---
if "data_df" in st.session_state:
    st.dataframe(st.session_state['data_df'])
# ...existing code...