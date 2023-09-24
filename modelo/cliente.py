x="-"
Nombres = ["Sofia", "Santiago", "Stiven", "Michell", "Ana"]
Direcciones = ["Cl 10 # 10B", "Cr 5 #2A", "Cr 10 # 10-30", "Cl 14 # 2-345", "Cl 20 # 10B-7"]
Telefonos = ["3117953412", "310271231", "318320457", "3142702298", "3117659860"]

class Cliente:
    def __init__(self,nombre,direccion,telefono):
        self.nombre: str = nombre
        self.direccion: str = direccion
        self.telefono: int = telefono
        Nombres.append(nombre)
        Direcciones.append(direccion)
        Telefonos.append(telefono)

    def informacion_clientes(self):
        print(x*75)
        print('Nombres', 'Direcciones', 'Telefonos')
        print(x*75)
        for i in range(0, len(Nombres)):                
                print(Nombres[i], Direcciones[i], Telefonos[i])

    def modificar_cliente(self):
        pass

    def confirmacion_modificacion_cliente(self):
        return("El cliente ha sido modificado exitosamente")