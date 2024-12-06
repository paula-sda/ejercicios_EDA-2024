from pymongo import MongoClient
from beans.localizador import Localizador

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')

db_name='eda'
collection_name='localizaciones'


def buscar_por_provincia(provincia):
    # mostramos los datos de una base de datos
    print("Mostramos los datos de la base de datos")
    db_pruebas = client[db_name][collection_name].find({"provincia": provincia})
    lista_ubicaciones = []

    for x in db_pruebas:
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)
    return lista_ubicaciones


def buscar_por_codigo_postal(codigo_postal):
    # Mostramos los datos de una base de datos
    print("Mostramos los datos filtrados por código postal")
    db_pruebas = client[db_name][collection_name].find({"codigo_postal": codigo_postal})
    lista_ubicaciones = []

    for x in db_pruebas:
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)
    return lista_ubicaciones


def buscar_por_latitud_longitud(latitud, longitud):
    # Consulta en la base de datos esa ubicacion 
    resultado = client[db_name][collection_name].find_one({"latitud": latitud, "longitud": longitud})
    if resultado:
        return Localizador(resultado['latitud'], resultado['longitud'])
    return None


def insertar_localizacion(localizador):
    # metemos datos en la base de datos
    client[db_name][collection_name].insert_one(localizador)


def cargar_datos_bd():
    #mostramos los datos de una base de datos
    print("Mostramos los datos de una base de datos paula-eda")
    db_pruebas = client[db_name][collection_name].find({})
    
    lista_ubicaciones = []
    for x in db_pruebas:
          
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)

    return lista_ubicaciones


def obtener_todas_las_ubicaciones():
    # Obtiene todos los documentos de la colección
    return list(client[db_name][collection_name].find({}))


def contar_elementos():
        coleccion = client[db_name][collection_name]
        total = coleccion.count_documents({})
        return total

