import streamlit as st
import json

from user import User

def show_login():
    # Text aus Textfeld löschen
    st.session_state.vorname_reg = ""
    st.session_state.nachname_reg = ""
    st.session_state.passwort_reg = ""

    st.title("Login")

    # Eingabeboxen
    Vorname_login = st.text_input("Vorname", "", key="vorname")
    Nachname_login = st.text_input("Nachname", "", key="nachname")
    Passwort_login = st.text_input("Passwort", "", type="password", key="passwort")

    #läd die Datenbank
    with open("user_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    bestätigen = st.button("Bestätigen", type="primary")

    #Abfrage ob die eingegebenen Werte der, der Datenbank entsprechen
    if bestätigen:
        for person in data:
            if (
                person["Vorname"] == Vorname_login
                and person["Nachname"] == Nachname_login
                and person["Passwort"] == Passwort_login
            ):
                st.info("Login erfolgreich")
                object_user = User(person["ID"],person["Vorname"],person["Nachname"])
                break
            else:
                st.info("##### Benutzername oder Passwort falsch")
                break
