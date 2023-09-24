x="-"
Clientes = ["Sofia", "Santiago", "Stiven", "Michell", "Ana"]
Codigos = ["002", "007", "001", "002", "003"]
Fechas = ["12/03/06","22/12/10","14/07/11","30/09/21","03/03/23"]

class Venta:
    def __init__(self,nombre_cliente,codigo_auto,fecha_compra):
        self.nombre_cliente: str = nombre_cliente
        self.codigo_auto: str = codigo_auto
        self.fecha_comora: str = fecha_compra

    def informacion_ventas(self):
        pass

    def modificar_venta(self):
        pass

    def confirmacion_modificacion_venta(self):
        return("La venta ha sido modificada exitosamente")