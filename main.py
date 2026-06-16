import streamlit as st

from user import User

Vorname = st.text_input("Vorname", "")
Nachname = st.text_input("Nachname", "")

bestätigen = st.button("Bestätigen", type="primary")

if bestätigen:
    User.add_users_to_json(Vorname, Nachname)