# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
# Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# Sugerencias
# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

# Utilizando los conceptos de la clase 8, guarde la información en un archivo de texto dentro de su Drive."

import json

from pathlib import Path

 

 

def obtener_ruta():

    BASE_DIR = Path(__file__).resolve().parent

    return BASE_DIR

 

 

def ingresar_datos() -> dict:

    """Ingreso DNI, nombre,  edad y si el usuario está activo, y devuelvo los datos en forma de diccionario"""

    dni = input("Ingresa DNI: ")

    nombre = input("Ingresa nombre: ")

    edad = input("Ingresa edad: ")

    activo = input("Ingresa si está activo: S/N")

 

    formulario = {"DNI": dni, "nombre": nombre, "edad": edad, "activo": activo}

    return formulario

 

 

def guardar_datos(formulario, ruta, nombre_del_archivo):

    with open(f"{ruta}/{nombre_del_archivo}", "w") as archivo:

        json.dump(formulario, archivo, indent=4)

        print("Registro guardado")

 

 

def main():

    nombre_del_archivo = "datos.json"

    ruta = obtener_ruta()

    formulario = ingresar_datos()

    guardar_datos(formulario, ruta, nombre_del_archivo)

 

 

main()