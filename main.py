import streamlit as st

import registration
import login

if "page" not in st.session_state:
    st.session_state.page = "main"


st.sidebar.write("### Profil")
login_button = st.sidebar.button("Login", type="primary")
registrieren = st.sidebar.button("Registrieren", type="primary")

if login_button:
    st.session_state.page = "login"

if registrieren:
    st.session_state.page = "registrieren"

if st.session_state.page == "login":
    login.show_login()
if st.session_state.page == "registrieren":
    registration.show_registration()