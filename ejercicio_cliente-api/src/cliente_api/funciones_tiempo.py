import json
import requests
from cliente_api.funciones_ubicacion import obtener_direccion 

# Función para obtener los datos del clima y la dirección
def obtener_clima(latitude, longitude):
    try:
        # Obtener la latitud y longitud desde la interfaz
        latitud = latitude.strip()
        longitud = longitude.strip()
        
        # Validar si los campos están vacíos
        if not latitud or not longitud:
            print("Advertencia", "Por favor, ingrese la latitud y la longitud.")
            return

        # Obtener la dirección usando Nominatim
        direccion = obtener_direccion(latitud, longitud)

        # URL de la API con los valores ingresados por el usuario
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        
        # Hacer la solicitud a la API del clima
        #response = requests.get(url)
        # Cambia esta línea en la función obtener_clima
        response = requests.get(url, timeout=5)  # Cambiando el tiempo de espera a 5 segundos

        data = response.json()

        #print("lugar de las coordenadas:")
        #print(json.dumps(direccion.raw, indent=4))
        #print("Datos del tiempo:")
        #print(json.dumps(data, indent=4))



        #Mostrar solo la dirección, temperatura y velocidad del viento
        print("Lugar de las coordenadas:", direccion.address)  #muestra solo la dirección
        print("Temperatura actual:", data["current_weather"]["temperature"], "°C")  #muestra solo la temperatura
        print("Velocidad del viento:", data["current_weather"]["windspeed"], "km/h")  #muestra solo la velocidad del viento

        
    except Exception as e:
        print(f"Error al obtener los datos: {e}")