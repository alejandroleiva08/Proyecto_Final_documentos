
##El primer módulo debe contener a la clase Clientes
from .Manejo_datos import guardar_datos

#class Clientes:

#    def __init__(self, nombre, password, edad, producto, cantidad):
#        self.nombre = nombre
#        self.password = password
#        self.edad = edad
#        self.producto = producto
#        self.cantidad = cantidad
#      
#    def introducir_datos(base_datos)-> dict:
#        usuarios = {}
#        usuarios[self.nombre] = input("Nombre: ")
#        usuarios[self.password] = input("Contrasena: ")
#        usuarios[self.edad] = input("Edad: ")
#        usuarios[self.producto] = input("Producto a comprar: ")
#        usuarios[self.cantidad] = input("Cantidad a comprar: ")
#        base_datos.append(usuarios)
#        guardar_datos()

def introducir_datos(RUTA_BASE_DATOS,base_datos)-> dict:
    usuarios = {}
    usuarios["nombre"] = input("Nombre: ")
    usuarios["password"] = input("Contrasena: ")
    usuarios["edad"] = input("Edad: ")
    usuarios["producto"] = input("Producto a comprar: ")
    usuarios["cantidad"] = input("Cantidad a comprar: ")
    base_datos.append(usuarios)
    guardar_datos(RUTA_BASE_DATOS, base_datos)
    