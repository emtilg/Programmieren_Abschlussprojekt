from pathlib import Path

import streamlit as st
from streamlit_folium import st_folium

from plotting import plot_tour
from tour import Tour
from gpx_reader import read_gpx
from geo import get_search_point_cached


def get_search_point():
    query = f"{st.session_state.routen_suche},Tirol"
    return get_search_point_cached(query)


def show_tour_planner():
    # die beiden session_states werden "gebaut"
    if "routen_suche" not in st.session_state:
        st.session_state.routen_suche = ""

    if "routen_umkreis" not in st.session_state:
        st.session_state.routen_umkreis = 40

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = ""

    #st.subheader("🚴 Touren")

    gpx_folder = Path("data/gpxtracks")
    gpx_folder.mkdir(parents=True, exist_ok=True)

    parquet_folder = Path("parquet_data")
    parquet_folder.mkdir(parents=True, exist_ok=True)

    files = st.session_state.get("uploaded_files")
    if files:
        for uploaded_file in st.session_state.uploaded_files:
            save_path = gpx_folder / uploaded_file.name
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            df = read_gpx(save_path)

            parquet_path = parquet_folder / f"{save_path.stem}.parquet"
            df.to_parquet(parquet_path)

        st.session_state.uploader_key += 1
        st.session_state.uploaded_files = []
        st.rerun()

    parquet_files = sorted(parquet_folder.glob("*.parquet"))

    if not parquet_files:
        st.warning("Keine GPX-Dateien gefunden.")
        return

    # ab hier wied instanziert

    search_point = get_search_point()
    tours = [Tour(file_path, search_point) for file_path in parquet_files]

    with st.expander("Filter", expanded=False):
        st.markdown("### Filter")
        st.session_state.routen_suche = st.text_input("Ort eingeben")  # um Touren in Orte zu suchen
        st.session_state.routen_umkreis = st.slider("Umkreis auswählen", 0, 70)  # Suchkreis einschränken

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
        s1, s2, s3, s4, s5 = st.columns(5)
        with s5:
            filter_anwenden = st.button("Filter anwenden", type="primary")

    if "filter_anwenden" not in st.session_state:
        st.session_state.filter_anwenden = False

    if filter_anwenden:
        st.session_state.filter_anwenden = True

    if st.session_state.filter_anwenden:
        filtered_tours = [
            tour
            for tour in tours
            if min_distance <= tour.get_distance() <= max_distance
            and min_elevation <= tour.get_elevation_gain() <= max_elevation
            and tour.get_distance_to_location() <= st.session_state.routen_umkreis
        ]

        if not filtered_tours:
            st.warning("Keine Touren passen zu den gewählten Filtern.")
            return

        spalte1, spalte2 = st.columns(2)
        with spalte2:
            st.write("")
            st.write("")
            st.write(f"{len(filtered_tours)} Tour(en) gefunden")

        with spalte1:
            selected_tour = st.selectbox(
                "Tour auswählen",
                filtered_tours,
                format_func=lambda tour: tour.name,
                #format_func=lambda tour: f"{tour.name} - {tour.get_distance():.1f} km - {tour.get_elevation_gain():.0f} hm",
            )

        route_map = plot_tour(selected_tour)

        st_folium(
            route_map,
            width=900,
            height=600,
        )

        col3, col4, col5 = st.columns([1,0.3,2])

        with col5:
            st.write("")
            st.session_state.duration = st.time_input(
                "Dauer der Tour auswählen", selected_tour.estimate_tour_time()
            )  # dauer der Tour auswählen

            sub_col1, sub_col2 = st.columns([2.6,1])
            with sub_col2: 
                st.write("")
                st.write("")  
                st.button("Tour auswählen", type="primary")
            
        with col3:
            st.subheader("Tourenstatistik")
            sub_col1, sub_col2 = st.columns([0.6,8])
            with sub_col1:
                st.write("")
            with sub_col2:
                #st.write("Distanz:", f"{selected_tour.get_distance():.2f} km")
                st.markdown(f"**Distanz:** {selected_tour.get_distance():.2f} km")
                st.markdown(f"**Höhenmeter:** {selected_tour.get_elevation_gain():.0f} m")
                st.markdown(f"**Energie:** {selected_tour.kcal_claculator()} kcal")      
