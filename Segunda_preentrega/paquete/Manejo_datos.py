#El segundo módulo debe crear instancias de Clientes.
#from modulo1 import Clientes

import json



def guardar_datos(RUTA_BASE_DATOS, base_datos):
    with open(RUTA_BASE_DATOS, "w") as archivo:
        json.dump(base_datos, archivo, indent=4)

def cargar_datos(RUTA_BASE_DATOS) -> list:
    base_datos = []
    try:
        with open(RUTA_BASE_DATOS, "r") as archivo:
            base_datos = json.load(archivo)
    except json.decoder.JSONDecodeError:
        print("El archivo existe pero esta danado")
    except FileNotFoundError:
        print("El archivo no existe, no se cargan datos")
    return base_datos

def mostrar_datos(base_datos):
    print(base_datos)