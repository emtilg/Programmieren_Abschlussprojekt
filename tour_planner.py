from pathlib import Path

import streamlit as st
from streamlit_folium import st_folium

from gpx_reader import read_gpx
from plotting import plot_gpx


def show_tour_planner():
    """Zeigt den Tour Planner mit GPX-Auswahl und Karte."""

    st.subheader("🚴 Touren")

    gpx_folder = Path("data/gpxtracks")
    gpx_files = sorted(gpx_folder.glob("*.gpx"))

    if not gpx_files:
        st.warning("Keine GPX-Dateien gefunden.")
        return

    selected_file = st.selectbox(
        "Tour auswählen",
        gpx_files,
        format_func=lambda file: file.stem,
    )

    df = read_gpx(selected_file)

    route_map = plot_gpx(df)

    st_folium(
        route_map,
        width=900,
        height=600,
    )