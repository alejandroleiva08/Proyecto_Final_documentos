
#El primer módulo debe contener a la clase Clientes

class Clientes:

    def __init__(self, nombre, edad, producto, cantidad):
        self.nombre = nombre
        self.edad = edad
        self.producto = producto
        self.cantidad = cantidad
      
    def ingrese_nombre(self):
        pass

    def ingrese_producto(self):
        pass

    def ingrese_cantidad(self):
        #MEtodo vacio
        pass

    def saludo_cliente(self):
        print(f"Hola {self.nombre} compraste un {self.producto}")
        pass


#cliente1 = Clientes("Alejandro", "Leiva", "24", "carro")

#cliente1.saludo_cliente()