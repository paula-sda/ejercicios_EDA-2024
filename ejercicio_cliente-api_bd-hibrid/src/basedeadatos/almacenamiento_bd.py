from pymongo import MongoClient
from beans.localizador import Localizador

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')

db_name='eda'
collection_name='localizaciones'

def obtener_nombres_database():
    # Obtener una lista de todos los nombres de bases de datos
    all_dbs = client.list_database_names()


def buscar_por_provincia(provincia):
    # mostramos los datos de una base de datos
    print("Mostramos los datos de una base de datos paula-eda")
    db_pruebas = client[db_name][collection_name].find({"provincia": provincia})
    for x in db_pruebas:
        print(x)


def insertar_localizacion(localizador):
    # metemos datos en la base de datos
    client[db_name][collection_name].insert_one(localizador)


def buscar_numero_concreto(numero_concreto):
    # mostramos los datos de una base de datos mediante el filtro
    print("Mostramos los datos especificos de una base de datos paula-eda")
    db_pruebas = client[db_name][collection_name].find({"numero":numero_concreto})
    for x in db_pruebas:
        print(x)

def cargar_datos_bd():
    #mostramos los datos de una base de datos
    print("Mostramos los datos de una base de datos paula-eda")
    db_pruebas = client[db_name][collection_name].find({})
    
    #print("Datos obtenidos de la base de datos:")
    #for documento in db_pruebas:
    #     print(documento)
    

    lista_ubicaciones = []
    for x in db_pruebas:
          
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)

    return lista_ubicaciones
