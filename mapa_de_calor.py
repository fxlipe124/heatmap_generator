import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import time
from uuid import uuid4
from addresses_cdc_2021 import addresses as addresses_cdc_2021
from addresses_cdc_2025 import addresses as addresses_cdc_2025
from addresses_mn_2025 import addresses as addresses_mn_2025

DATA_SOURCE = "cdc_2025"  # ESCOLHER ENTRE: "cdc_2021", "cdc_2025", "mn_2025"

city_settings = {
    "cdc_2021": {
        "addresses": addresses_cdc_2021,
        "map_center": [-29.7454, -50.0097],  # Capão da Canoa
        "city_prefix": "capao_da_canoa"
    },
    "cdc_2025": {
        "addresses": addresses_cdc_2025,
        "map_center": [-29.7454, -50.0097],  # Capão da Canoa
        "city_prefix": "capao_da_canoa"
    },
    "mn_2025": {
        "addresses": addresses_mn_2025,
        "map_center": [-29.6842, -51.4608],  # Montenegro
        "city_prefix": "montenegro"
    }
}

if DATA_SOURCE not in city_settings:
    raise ValueError(f"Invalid DATA_SOURCE: {DATA_SOURCE}. Choose from {list(city_settings.keys())}")
ADDRESSES = city_settings[DATA_SOURCE]["addresses"]
MAP_CENTER = city_settings[DATA_SOURCE]["map_center"]
CITY_PREFIX = city_settings[DATA_SOURCE]["city_prefix"]

geolocator = Nominatim(user_agent=f"heatmap_{CITY_PREFIX}_{uuid4()}")

def clean_address(address):
    if "null_rua" in address.lower() or ", , " in address:
        return None
    return address

geocode_cache = {}
def geocode_address(address):
    if address is None:
        return None
    if address in geocode_cache:
        return geocode_cache[address]
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            geocode_cache[address] = (location.latitude, location.longitude)
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderUnavailable):
        time.sleep(1)  # Wait before retrying
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                geocode_cache[address] = (location.latitude, location.longitude)
                return location.latitude, location.longitude
        except:
            return None
    return None

coordinates = []
valid_addresses = [clean_address(addr) for addr in ADDRESSES]
for addr in valid_addresses:
    if addr:
        coords = geocode_address(addr)
        if coords:
            coordinates.append([coords[0], coords[1]])

if coordinates:
    heatmap_map = folium.Map(location=MAP_CENTER, zoom_start=13)

    HeatMap(coordinates, radius=15, blur=20).add_to(heatmap_map)

    output_file = f"heatmap_{CITY_PREFIX}_{DATA_SOURCE}.html"
    heatmap_map.save(output_file)
    print(f"Heatmap saved to {output_file}")
else:
    print("No valid coordinates found. Heatmap not generated.")