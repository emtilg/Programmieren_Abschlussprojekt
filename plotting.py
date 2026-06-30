import folium
from tour import Tour

def plot_tour(tour: Tour):

    center = tour.get_center()

    m = folium.Map(
        location=center,
        zoom_start=12,
        wheel_px_per_zoom_level=150
    )

    coords = tour.get_coords()

    folium.PolyLine(
        coords,
        weight=4,
    ).add_to(m)
    
    return m