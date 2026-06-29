import folium


def plot_gpx(df):
    center = [
        df["lat"].mean(),
        df["lon"].mean(),
    ]

    m = folium.Map(
        location=center,
        zoom_start=12,
    )

    coords = df[["lat", "lon"]].values.tolist()

    folium.PolyLine(
        coords,
        weight=4,
    ).add_to(m)

    return m