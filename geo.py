from functools import lru_cache
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="tourensuche", timeout=10)

@lru_cache(maxsize=128)
def get_search_point_cached(query: str):
    location = geolocator.geocode(query)
    if location is None:
        return None
    return (location.latitude, location.longitude)