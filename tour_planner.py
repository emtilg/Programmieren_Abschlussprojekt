from pathlib import Path

import streamlit as st
from streamlit_folium import st_folium

from plotting import plot_tour
from tour import Tour


def show_tour_planner():
    st.subheader("🚴 Touren")

    gpx_folder = Path("data/gpxtracks")
    gpx_folder.mkdir(parents=True, exist_ok=True)

    uploaded_files = st.file_uploader(
        "Weitere GPX-Dateien hochladen",
        type="gpx",
        accept_multiple_files=True,
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            save_path = gpx_folder / uploaded_file.name
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

    gpx_files = sorted(gpx_folder.glob("*.gpx"))

    if not gpx_files:
        st.warning("Keine GPX-Dateien gefunden.")
        return

    #HIER WIRD INSTANZIERT
    
    tours = [Tour(file_path) for file_path in gpx_files]

    st.markdown("### Filter")

    col1, col2 = st.columns(2)

    with col1:
        min_distance = st.number_input(
            "Minimale Distanz (km)",
            min_value=0.0,
            value=0.0,
            step=1.0,
        )
        min_elevation = st.number_input(
            "Minimale Höhenmeter (m)",
            min_value=0.0,
            value=0.0,
            step=50.0,
        )

    with col2:
        max_distance = st.number_input(
            "Maximale Distanz (km)",
            min_value=0.0,
            value=500.0,
            step=1.0,
        )
        max_elevation = st.number_input(
            "Maximale Höhenmeter (m)",
            min_value=0.0,
            value=10000.0,
            step=50.0,
        )

    filtered_tours = [
        tour for tour in tours
        if min_distance <= tour.get_distance() <= max_distance
        and min_elevation <= tour.get_elevation_gain() <= max_elevation
    ]

    if not filtered_tours:
        st.warning("Keine Touren passen zu den gewählten Filtern.")
        return

    st.write(f"{len(filtered_tours)} Tour(en) gefunden")

    selected_tour = st.selectbox(
        "Tour auswählen",
        filtered_tours,
        format_func=lambda tour: (
            f"{tour.name} - "
            f"{tour.get_distance():.1f} km - "
            f"{tour.get_elevation_gain():.0f} hm"
        ),
    )

    route_map = plot_tour(selected_tour)

    st_folium(
        route_map,
        width=900,
        height=600,
    )

    col3, col4 = st.columns(2)

    with col3:
        st.metric("Distanz", f"{selected_tour.get_distance():.2f} km")

    with col4:
        st.metric("Höhenmeter", f"{selected_tour.get_elevation_gain():.0f} m")

    st.write(selected_tour.kcal_claculator())
