import streamlit as st
from functions.Mitternachtsformel import Mitternachtsformel, parse_quadratic
st.title("Mitternachtsformel berechnen")

st.write("Die Mitternachtsformel, auch bekannt als die quadratische Lösungsformel, ist eine Methode zur Berechnung der Lösungen einer quadratischen Gleichung der Form ax^2 + bx + c = 0. Die Formel lautet: x = (-b ± √(b^2 - 4ac)) / (2a).")

st.write("Hier kannst du die Mitternachtsformel anwenden, um die Lösungen einer quadratischen Gleichung zu berechnen.")

input_string = st.text_input("Gib die quadratische Gleichung ein (z.B. 2x^2 + 3x - 5):")
    
submitted = st.form_submit_button("Berechnen")

if submitted:
    quadratische_Formel = parse_quadratic(input_string)
    x1, x2, text = Mitternachtsformel(quadratische_Formel)

    st.write(x1, x2)
 # Every form must have a submit button.
submitted = st.form_submit_button("Submit")

if input_string:
    quadratische_Formel = parse_quadratic(input_string)
    result = Mitternachtsformel(quadratische_Formel)
    st.write("Das Ergebnis ist:", result)

import csv

class DataManager:
        """Fallback DataManager, wenn Import nicht funktioniert."""

        def __init__(self):
            pass

        def save(self, data, filename="data.csv"):
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)

                if isinstance(data, dict):
                    writer.writerow(data.keys())
                    writer.writerow(data.values())

                elif isinstance(data, list):
                    for row in data:
                        writer.writerow(row)

# --- NEW CODE to display the history table ---
if "data_df" in st.session_state:
    st.dataframe(st.session_state['data_df'])
# ...existing code...