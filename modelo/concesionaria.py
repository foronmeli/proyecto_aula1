from modelo.auto import Auto
from modelo.venta import Venta
from modelo.cliente import Cliente

class Concesionaria:
    def crear_auto(self):
        codigo=input("Ingrese el codigo del auto: ")
        modelo=input("Ingrese el modelo del auto: ")
        marca=input("Ingrese la marca del auto: ")
        precio=input("Ingrese el precio del auto: ")
        Auto(codigo,marca,modelo,precio)
        print(self.mensaje_confirmacion_auto())

    def registrar_cliente(self):
        nombre=input("Ingrese su nombre: ")
        direccion=input("Ingrese su direccion: ")
        telefono=input("Ingrese su telefono: ")
        Cliente(nombre,direccion,telefono)
        print(self.mensaje_confirmacion_cliente)

    def mensaje_confirmacion_auto(self):
        return("El carro ha sido creado exitosamente")
    
    def mensaje_confirmacion_cliente(self):
        return("Ha sido registrado exitosamente")