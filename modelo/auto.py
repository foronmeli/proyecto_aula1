x="-"
Marcas = ["Mazda", "MiniCooper", "Mercedes Benz", "Porsche", "BMW", "Lamborghini", "Tesla"]
Modelo = ["3", "ClubMan", "HatchBack", "Cayenne", "i4", "Urus", "Model Y"]
codAutos = ["001", "002", "003", "004", "005", "006", "007"]
PreciosAutos = [83486.30, 31929.77, 47537.40, 256900, 95990.26, 650000, 64970]

class Auto:
    def __init__(self,codigo,marca,modelo,precio):
        self.codigo: int = codigo
        self.marca: str = marca
        self.modelo: str = modelo
        self.precio: int = precio
        Marcas.append(marca)
        Modelo.append(modelo)
        codAutos.append(codigo)
        PreciosAutos.append(precio)

    def informacion_autos(self):
        print(x*75)
        print('Codigo', 'Marca', 'Modelo', 'Precio(USD)')
        print(x*75)
        for i in range(0, len(Marcas)):                
                print(codAutos[i], Marcas[i], Modelo[i], PreciosAutos[i])

    def modificar_auto(self):
        pass

    def busqueda_auto(self):
        pass

    def confirmacion_modificacion_auto(self):
        return("El auto ha sido modificado exitosamente")