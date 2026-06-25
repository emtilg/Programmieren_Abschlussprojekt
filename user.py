import json
import streamlit as st


class User:
    @staticmethod
    def add_users_to_json(Vorname, Nachname, Passwort):
        file = "user_data.json"

        # läd datei
        with open(file, "r") as f:
            users = json.load(f)

        # fügt eine individuelle ID hinzu
        if len(users) == 0:
            id = 1
        else:
            id = users[-1]["ID"] + 1

        new_user = {"ID": id, "Vorname": Vorname, "Nachname": Nachname, "Passwort": Passwort}

        # fügt user hinzu
        users.append(new_user)

        # speichert user im Json
        with open(file, "w") as f:
            json.dump(users, f, indent=4)

    def __init__(self, ID, Vorname, Nachname,):
        self.ID = ID
        self.Vorname = Vorname
        self.Nachname = Nachname

    def begrüßen(self):
        st.title(f"Hallo {self.Vorname}")
