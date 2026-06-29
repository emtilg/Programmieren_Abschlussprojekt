from math import radians, sin, cos, sqrt, atan2
from pathlib import Path

from gpx_reader import read_gpx


class Tour:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.name = file_path.stem
        self.data = read_gpx(file_path)

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

