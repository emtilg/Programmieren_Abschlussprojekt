import json
import streamlit as st


class User:
    @staticmethod
    def add_users_to_json(Vorname, Nachname, Passwort, Gewicht):
        file = "user_data.json"

        # läd datei
        with open(file, "r") as f:
            users = json.load(f)

        # fügt eine individuelle ID hinzu
        if len(users) == 0:
            id = 1
        else:
            id = users[-1]["ID"] + 1

        new_user = {"ID": id, "Vorname": Vorname, "Nachname": Nachname, "Passwort": Passwort, "Gewicht": Gewicht}

        # fügt user hinzu
        users.append(new_user)

        # speichert user im Json
        with open(file, "w") as f:
            json.dump(users, f, indent=4)

    def __init__(self, ID, Vorname, Nachname, Gewicht):
        self.ID = ID
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Gewicht = Gewicht

    def begrüßen(self):
        st.title(f"Griaß di {self.Vorname}")
    
    def weight(self):
        return self.Gewicht
