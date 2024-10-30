from geopy.geocoders import Nominatim


# Función para obtener la dirección con Nominatim
def obtener_direccion(latitud, longitud):
    geolocator = Nominatim(user_agent="test")
    location = geolocator.reverse(f"{latitud}, {longitud}")
    return location