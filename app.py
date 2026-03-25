import pandas as pd 
import streamlit as st

# --- NEW CODE: import and initialize data manager and login manager ---
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(       # initialize data manager
    fs_protocol='webdav',         # protocol for the filesystem, use webdav for switch drive
    fs_root_folder="app_data"  # folder on switch drive where the data is stored
    ) 
login_manager = LoginManager(data_manager) # handles user login and registration
login_manager.login_register()             # stops if not logged in
# --- END OF NEW CODE ---

# --- CODE UPDATE: load user data from data manager if not already present in session state --
# if 'data_df' not in st.session_state:
    # st.session_state['data_df'] = data_manager.load_user_data(
        # 'data.csv',                     # The file on switch drive where the data is stored
        # initial_value=pd.DataFrame(),   # Initial value if the file does not exist
        # parse_dates=['timestamp']       # Parse timestamp as datetime
        # )
# --- CODE UPDATE: load user data from data manager if not already present in session state --
if 'data_df' not in st.session_state:
    try:
        st.session_state['data_df'] = data_manager.load_user_data(
            'data.csv',
            initial_value=pd.DataFrame(columns=['formel', 'x1', 'x2', 'beschreibung']),
            parse_dates=['timestamp']
        )
    except Exception as e:
        # Falls Fehler, leeren DataFrame verwenden
        st.session_state['data_df'] = pd.DataFrame(columns=['formel', 'x1', 'x2', 'beschreibung'])
# --- END OF CODE UPDATE ---

st.set_page_config(page_title="Mitternachtsformel Rechner", page_icon=":material/monitor_weight:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/quad_Formel_berechnen.py", title="Mitternachtsformel Rechner", icon=":material/info:")

pg = st.navigation([pg_home, pg_second])
pg.run()