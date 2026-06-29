import streamlit as st
import base64
import streamlit_float

import registration
import login

from pathlib import Path
from streamlit_folium import st_folium
from gpx_reader import read_gpx
from tour_planner import show_tour_planner
from plotting import plot_tour


# CSS code zwischen den Balken, nur Design, kein funktionaler code
# _________________________________________________________________________________________________

# macht den Menübalken transparent
st.markdown(
    """
<style>
[data-testid="stHeader"] {
    background: transparent;
}
</style>
""",
    unsafe_allow_html=True,
)


# fügt Hintergrundbild ein
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


img = get_base64("images/Titelbild_6.png")

st.markdown(
    f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: contain;
    background-position: top;
    background-repeat: no-repeat;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,0.92);
    pointer-events: none;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ______________________________________________________________________________________________

st.set_page_config(layout="wide")

main_page, right_side = st.columns([5, 1])

# Initialisiert st.session_state.page mit "main", falls noch kein Page-State existiert
if "page" not in st.session_state:
    st.session_state.page = "main"

if "true_login" not in st.session_state:
    st.session_state.true_login = False

# erstellt eine Sidebar mit Buttons
sol1_s, col2_s, col3_s = st.sidebar.columns([1,3,1])
with col2_s:
    st.image("images/Logo-Programmieren.jpeg", width=100)
st.sidebar.write("### Profil")
login_button = st.sidebar.button("Login", type="primary")
registrieren = st.sidebar.button("Registrieren", type="primary")

# überschreibung der st.session_state.page damit seiten immer neu angezeigt werden können
if login_button:
    st.session_state.page = "login"

if registrieren:
    st.session_state.page = "registrieren"

# zeigt die neuen seiten an, alles was in der Funktion steht, wird angezeigt
if st.session_state.page == "login":
    login.show_login()

if st.session_state.page == "registrieren":
    registration.show_registration()

# die eigentliche Startseite, wo alles angezeigt werden kann. Hier einfach ohne funktionsaufruf hineinschreiben
if st.session_state.page == "main" and not st.session_state.true_login:
    st.title("Startseite")
    st.write("##### Bitte einloggen")
    st.write("Noch kein Konto? Einfach Registrieren und loslegen")

# die Startseite der User, hier sollte alles individuell angezeigt werden
with main_page:
    if st.session_state.page == "main" and st.session_state.true_login:
        if "object_user" in st.session_state:
            st.session_state.object_user.begrüßen()
        #st.image("images/Logo-Programmieren.jpeg")

        #Routen auswahl

        show_tour_planner()


        
with right_side:
    if st.session_state.page == "main" and st.session_state.true_login:
        stats = st.container()

        with stats:
            st.write("### Statistik")
            st.write("Hier finden sie die Statistiken mit Höhenmeter, Kilometer, getrunkene Bier, etc...")
        stats.float()


