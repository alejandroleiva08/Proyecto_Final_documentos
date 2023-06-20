

#El segundo módulo debe crear instancias de Clientes.
from modulo1 import Clientes

class Datos(Clientes):
  
    def __str__(self) -> str:
        return Datos

    def mostrar_datos(self):
        print (f"El cleinte {self.nombre} compro {self.cantidad} de el producto llamado {self.producto}")
        pass

#    def ingrese_nombre(self):
#        self.nombre = input("Ingrese nombre de cliente: ")
#
#    def ingrese_edad(self):
#        self.edad = input("Ingrese edad del cliente: ")
#
#    def ingrese_producto(self):
#        self.producto = input("Ingrese producto a comprar: ")
#        
#    def ingrese_cantidad(self):
#        self.cantidad = input("Ingrese cantidad a comprar: ")
#
#

cliente1 = Datos("Alejandro Leiva", "24", "Carro", "1")

cliente1.mostrar_datos()


