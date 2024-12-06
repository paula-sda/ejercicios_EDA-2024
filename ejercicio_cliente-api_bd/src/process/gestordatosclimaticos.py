# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
import json
from beans.localizador import Localizador
from basedeadatos import almacenamiento_bd


class GestorDeDatosClimaticos:


    def __init__(self):
        print("Iniciando gestor de datos climaticos")
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")


    def get_numero_ubicaciones(self):
        return almacenamiento_bd.contar_elementos()

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        # Consulta todos los documentos en la base de datos
        ubicaciones = almacenamiento_bd.obtener_todas_las_ubicaciones()

        # Diccionario para organizar los códigos postales por provincia
        agrupacion_codigos_postales = {}

        for ubicacion in ubicaciones:
            # Obtiene la provincia o asigna "Sin provincia" si es null
            provincia = ubicacion.get("provincia") or ubicacion.get("estado") or "Sin provincia"
            codigo_postal = ubicacion.get("codigo_postal")

            # Asegura que hay un código postal válido
            if codigo_postal:
                if provincia in agrupacion_codigos_postales:
                    agrupacion_codigos_postales[provincia].append(codigo_postal)
                else:
                    agrupacion_codigos_postales[provincia] = [codigo_postal]

        # Mostrar resultados
        if agrupacion_codigos_postales:
            print(json.dumps(agrupacion_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")


    # metodos necesarios
    
    def insertar_nueva_ubicacion(self, latitud, longitud):
        # Verifica si la ubicación ya existe en la base de datos
        ubicacion_encontrada = almacenamiento_bd.buscar_por_latitud_longitud(latitud, longitud)

        if ubicacion_encontrada:
            print("================================================")
            print("Ubicación ya existe")
            print(f"Latitud: {ubicacion_encontrada.latitud}, Longitud: {ubicacion_encontrada.longitud}")
            print("================================================")
        else:
            # Inserta la nueva ubicación
            nueva_ubicacion = Localizador(latitud, longitud)
            almacenamiento_bd.insertar_localizacion(nueva_ubicacion.to_dict())
            print("Ubicación agregada correctamente")

        return ubicacion_encontrada
    

    def buscar_por_codigo_postal(self, codigo_postal):
        ubicaciones = almacenamiento_bd.buscar_por_codigo_postal(codigo_postal)
        if ubicaciones:  
            ubicacion_encontrada = ubicaciones[0]  

        return ubicacion_encontrada

    
    def buscar_por_provincia(self,provincia):

        ubicaciones=almacenamiento_bd.buscar_por_provincia(provincia)
        return ubicaciones


    def buscar_por_latitud_longitud(self, latitud, longitud):
        ubicacion = almacenamiento_bd.buscar_por_latitud_longitud(latitud, longitud)
        if ubicacion:
            print("Ubicación encontrada:")
            print(f"Latitud: {ubicacion.latitud}, Longitud: {ubicacion.longitud}")
        else:
            print("No se encontró ninguna ubicación con las coordenadas proporcionadas.")
        return ubicacion
