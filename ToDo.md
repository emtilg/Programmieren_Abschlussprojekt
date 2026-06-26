-----
# ToDo

#### This Markdown splits all Tasks among the 3 of us

### Marc



### Nicolas
- GPX Dateinen einlesen/ auswerten
- Plot von Map und Anzeige von Tourdaten
- Tour Klasse / Datei
- Ausreden Generator



### Emmanuel
Aufgaben:
    - Login/ Registrierung
    - User Klasse

Erledigt:
    - Registrierung und Daten in Json File speichern
    - Login
    - Startseite mit wenig Design
    - Nach einloggen - andere Seite

-----

# Funktionen Plan:

### GPX auslesen und Plotten - Nicolas

def read_gpx():

    Eingabe: GPX Datei
    Ausgabe: DataFrame

def plot_gpx():

    Eingabe: DataFrame aus read_gpx
    Ausgabe: Karte zum einfügen
    Tool: Foilum


### Streamlit grobaufbau - Marc

- Mock_up
- Dashboard
- Umgebung
- Dropdown - ohne funktion


### User-login - Emmanuel

def user_registration():

    Eingabe: liste oder einzelne strings - je nach streamlit ausgabe
    Ausgabe: eintrag im DataFrame - eine Zeile hinzufügen

def user_login():

    Eingabe: Name und Kennwort
    Ausgabe: Objekt der Klasse User. Über DateFrame aus der Registrierung erstellen

Abfrage ob Kennwort des Users mit dem DataFrame übereinstimmt