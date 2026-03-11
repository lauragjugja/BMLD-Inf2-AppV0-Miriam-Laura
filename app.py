import pandas as pd  # --- NEW CODE: add pandas to the imports ---
import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

# --- NEW CODE: initialize empty data frame if not already present ---
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame()
# --- END OF NEW CODE ---

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/quad_Formel_berechnen.py", title="Mitternachtsformel Rechner", icon=":material/info:")

pg = st.navigation([pg_home, pg_second])
pg.run()