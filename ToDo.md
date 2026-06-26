-----
# ToDo

#### This Markdown splits all Tasks among the 3 of us

### Marc
    - Registration erweitern, Gewicht, Geschlecht, Größe


### Nicolas
- GPX Dateinen einlesen/ auswerten
- Plot von Map und Anzeige von Tourdaten
- Tour Klasse / Datei
    -  Für jede Tour wird bei Aufruf ein Objekt der Klasse Tour erstellt, welches dann im Kalender angezeigt werden kann. Inhalt Klasse: Kilometer, Höhenmeter etc...
- Ausreden Generator



### Emmanuel
Aufgaben:
    - Login/ Registrierung
    - User Klasse
    - Startseite: eventuell "Diashow" von Touren
    - Kalorienrechner und Umrechner
    - Statistik
    - Kalender + Speichern von Tour
    - Gefahrene Touren extern speichern zum anschauen


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