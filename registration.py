import streamlit as st
import time

from user import User


def show_registration():

    st.title("Registrieren")

    # Textboxen zum befüllen der Datenbank
    st.write("Alle Felder mit * sind Pflichtfelder")
    Vorname = st.text_input("Vorname*", "", key="vorname_reg")
    Nachname = st.text_input("Nachname*", "", key="nachname_reg")
    Passwort = st.text_input("Passwort*", "", type="password", key="passwort_reg")
    Gewicht = st.number_input("Gewicht in Kg*", key="gewicht_reg")

    # Bestätigung sowie AGB
    AGB = st.checkbox("Ich habe die Nutzungsbedingungen sowie die AGB glesen und akzeptiere sie")
    bestätigen = st.button("Bestätigen", type="primary")

    # Abfragen, dass der Rahmen festgelegt wird
    if bestätigen and AGB and len(Vorname) > 0 and len(Nachname) > 0 and len(Passwort) > 0 and Gewicht > 0:
        User.add_users_to_json(Vorname, Nachname, Passwort, Gewicht)
        st.success("##### Registrierung erfolgreich")

        time.sleep(2)

        st.session_state.page = "main"
        st.rerun()

    if bestätigen and AGB and (len(Vorname) == 0 or len(Nachname) == 0 or len(Passwort) == 0):
        st.warning("##### Sie müssen alle Pflichtfelder ausfüllen")

    if bestätigen and not AGB:
        st.warning("##### Bestätigen Sie die AGB")

    