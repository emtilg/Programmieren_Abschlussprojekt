from math import radians, sin, cos, sqrt, atan2
from pathlib import Path
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta

from geopy.distance import geodesic

# from gpx_reader import read_gpx
# from user import User


class Tour:
    def __init__(self, file_path: Path, search_point=None):
        self.file_path = file_path
        self.name = file_path.stem
        # self.data = read_gpx(file_path)
        self.data = pd.read_parquet(file_path)
        self.lat = search_point[0]
        self.long = search_point[1]

    def get_center(self):
        return [
            self.data["lat"].mean(),
            self.data["lon"].mean(),
        ]

    def get_coords(self):
        return self.data[["lat", "lon"]].values.tolist()

    def get_distance(self):
        coords = self.get_coords()

        if len(coords) < 2:
            return 0.0

        total_distance = 0.0
        earth_radius = 6371.0

        for i in range(1, len(coords)):
            lat1, lon1 = coords[i - 1]
            lat2, lon2 = coords[i]

            lat1 = radians(lat1)
            lon1 = radians(lon1)
            lat2 = radians(lat2)
            lon2 = radians(lon2)

            dlat = lat2 - lat1
            dlon = lon2 - lon1

            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            total_distance += earth_radius * c

        return total_distance

    def get_elevation_gain(self):
        elevations = self.data["elevation"].dropna().tolist()

        if len(elevations) < 2:
            return 0.0

        total_gain = 0.0

        for i in range(1, len(elevations)):
            difference = elevations[i] - elevations[i - 1]
            if difference > 0:
                total_gain += difference

        return total_gain

    def kcal_claculator(self):
        g = 9.81
        duration = st.session_state.duration.hour * 3600 + st.session_state.duration.minute * 60
        distance_m = self.get_distance() * 1000
        avg_velosity = distance_m / duration

        E_pot = st.session_state.object_user.weight() * g * self.get_elevation_gain()
        Fr_s = 0.01 * st.session_state.object_user.weight() * g * distance_m
        Fd_s = 0.5 * 1.11 * 0.6 * avg_velosity**2 * distance_m

        kcal = (E_pot + Fr_s + Fd_s) / (0.23 * 4184)
        return round(kcal)

    def estimate_tour_time(self):
        richtwert = self.data["time"].iloc[-1] - self.data["time"].iloc[0]

        def duration_to_time(td: timedelta) -> datetime.time:
            base = datetime.datetime(1900, 1, 1)
            return (base + td).time()

        startwert = duration_to_time(richtwert)
        return startwert

    def get_distance_to_location(self):
        # geolocator = Nominatim(user_agent="tourensuche", timeout=10)

        # location = geolocator.geocode(f"{st.session_state.routen_suche},Tirol")
        distanz = geodesic((self.lat, self.long), (self.data["lat"].mean(), self.data["lon"].mean())).km

        return distanz
