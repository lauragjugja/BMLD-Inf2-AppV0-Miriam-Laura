import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
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
 
  # --- CODE UPDATE: create result dict and update history ---
    result = {
        "Zeitstempel": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Formel": input_string,
        "x1": x1,
        "x2": x2,
        "Beschreibung": text
    }
    st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])], ignore_index=True)
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['data_df'], 'data.csv')  # save updated history to switch drive
    
    # --- END OF CODE UPDATE ---
 
# --- NEW CODE: plot quadratic function with zeros ---
    st.subheader("Grafische Darstellung deiner neusten Eingabe")
    
    a, b, c = quadratische_Formel
    
    if a != 0:
        # x-Bereich bestimmen (um Nullstellen herum)
        x_min = min(x1 or 0, x2 or 0) - 5 if (x1 is not None and x2 is not None) else -10
        x_max = max(x1 or 0, x2 or 0) + 5 if (x1 is not None and x2 is not None) else 10
        
        x_vals = np.linspace(x_min, x_max, 300)
        y_vals = a * x_vals**2 + b * x_vals + c
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Parabel zeichnen
        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'f(x) = {a}x² + {b}x + {c}')
        
        # x-Achse zeichnen
        ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        
        # Nullstellen als rote Punkte markieren
        if x1 is not None and x2 is not None:
            ax.plot([x1, x2], [0, 0], 'ro', markersize=10, label=f'Nullstellen: x₁={x1:.2f}, x₂={x2:.2f}')
        elif x1 is not None:
            ax.plot([x1], [0], 'ro', markersize=10, label=f'Nullstelle (doppelt): x={x1:.2f}')
        
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('f(x)', fontsize=12)
        ax.set_title('Quadratische Funktion', fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10)
        
        st.pyplot(fig)
    # --- END OF NEW CODE ---
 
# --- NEW CODE to display the history table ---
if "data_df" in st.session_state and not st.session_state['data_df'].empty:
    st.subheader("Berechnungsverlauf")
    st.dataframe(st.session_state['data_df'])
 