from cliente_api.funciones_tiempo import obtener_clima

print("Obtener el clima de un lugar concreto")
latitude = input("inserta la latitud ")
longitude = input("inserta la longitud ")

obtener_clima(latitude, longitude) 