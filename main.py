'''import streamlit as st

from user import User

st.title("Registrieren")

# Textboxen zum befüllen der Datenbank
st.write("Alle Felder mit * sind Pflichtfelder")
Vorname = st.text_input("Vorname*", "")
Nachname = st.text_input("Nachname*", "")
Passwort = st.text_input("Passwort*", "", type="password")

# Bestätigung sowie AGB
AGB = st.checkbox("Ich habe die Nutzungsbedingungen sowie die AGB glesen und akzeptiere sie")
bestätigen = st.button("Bestätigen", type="primary")

# Abfragen, dass der Rahmen festgelegt wird
if bestätigen and AGB and len(Vorname) > 0 and len(Nachname) > 0 and len(Passwort) > 0:
    User.add_users_to_json(Vorname, Nachname, Passwort)
    st.success("Registrierung erfolgreich")
if bestätigen and AGB and (len(Vorname) == 0 or len(Nachname) == 0 or len(Passwort) == 0):
    st.warning("##### Sie müssen alle Pflichtfelder ausfüllen")
if bestätigen and not AGB:
    st.warning("##### Bestätigen Sie die AGB")
'''

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