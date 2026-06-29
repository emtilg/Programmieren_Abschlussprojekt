from pathlib import Path

import gpxpy
import pandas as pd


def read_gpx(file_path: Path) -> pd.DataFrame:
    with open(file_path, "r", encoding="utf-8") as file:
        gpx = gpxpy.parse(file)

    rows = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                rows.append(
                    {
                        "lat": point.latitude,
                        "lon": point.longitude,
                        "elevation": point.elevation,
                        "time": point.time,
                    }
                )

    return pd.DataFrame(rows)

#kurzer Test

#df = read_gpx(Path("data/gpxtracks/Alpl.gpx"))

#print(df.head())
