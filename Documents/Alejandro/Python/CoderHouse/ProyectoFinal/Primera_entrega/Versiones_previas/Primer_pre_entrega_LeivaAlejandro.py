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


def obtener_ruta(nombre_del_archivo: str) -> Path:
    BASE_DIR = Path(__file__).resolve().parent
    ruta_archivo = BASE_DIR / nombre_del_archivo
    return ruta_archivo


#Funcion que crea un nuevo archivo en caso no exista y revisa si cuenta con algun error
def cargar_datos (ruta_archivo : Path) -> list:
    base_de_datos = []
    if ruta_archivo.exists():
        try:
            with open(f"{ruta_archivo}",) as archivo:
                base_de_datos = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo existe pero tiene errores")
    else:
        print("El archivo de la base de datos no existe")
        print("Se crea el archivo ", ruta_archivo)
    return base_de_datos


#Funcion que suministra el ingreso de datos para registrar un usuario
def ingresar_datos() -> dict:
    """Ingreso Nombre y contraseña y devuelvo los datos en forma de diccionario"""
    nombre = input("Ingresa nombre de usuario: ")
    contra = input("Ingresa contraseña: ")
    print("Informacion valida, se esta ingresando la informacion")
    formulario = {"Nombre": nombre,
                  "Contra": contra}
    return formulario

#def validar_usuario(base_de_datos):
#    for nombre in base_de_datos:
#        base_de_datos.split()
#        verificar_nombre = input("Ingresa el de usuario para login: ")
#
#        if True:
#            print("!El usuario existe!")
#            verificar_contra = input("Ingrese la contrasena del usuario: ")
#        else:
#            print ("el usuario no existe")
#    return
        

#Funcion que almacena los datos suministrados en el archivo
def guardar_datos(formulario :dict , ruta_archivo : Path , base_de_datos : list):
    base_de_datos.append(formulario)
    with open(f"{ruta_archivo}", "w") as archivo:
        json.dump(base_de_datos, archivo, indent=2)
        print("Registro guardado")
        return formulario

#def login():
 #   for nombre in formulario:
  #  



def main():
    nombre_del_archivo = "datos.json2"
    ruta_archivo = obtener_ruta(nombre_del_archivo)
#  print(ruta)
    base_de_datos = cargar_datos(ruta_archivo)
    formularios_cargados = len(base_de_datos)
    while True:
        print(f"Nuevo formulario N {formularios_cargados + 1}")
        formulario = ingresar_datos()
        base_de_datos = guardar_datos(formulario,ruta_archivo,base_de_datos)
        #formularios_cargados = len(base_de_datos)
#        if not continuar_programa():
#            break
        return print(f"Cantidad de registros en la base de datos: {formularios_cargados + 1}")


main()