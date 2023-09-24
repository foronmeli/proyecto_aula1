import sys
from typing import Optional

from modelo.auto import Auto
from modelo.venta import Venta
from modelo.cliente import Cliente
from modelo.concesionaria import Concesionaria

class Consola:
    
    def mostrar_menu1(self):
        titulo = "MASSI"
        print(f"\n{titulo:_^30}")
        print("1. Empleado")
        print("2. Cliente")
        print(f"{'_':_^30}")

    def mostrar_menu21(self):
        titulo = "MASSI"
        print(f"\n{titulo:_^30}")
        print("1. Catálogo")
        print("2. Crear auto")
        print("3. Modificar auto")
        print("4. Informacion ventas")
        print("5. Modificar venta")
        print("6. Informacion clientes")
        print("7. Modificar cliente")
        print("8. Salir")
        print(f"{'_':_^30}")

    def mostrar_menu22(self):
        titulo = "MASSI"
        print(f"\n{titulo:_^30}")
        print("1. Hacer compra")
        print("2. Catálogo")
        print("3. Busqueda auto")
        print("4. Registrarse")
        print("5. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu1()
            opcion1 = int(input("¿Usted es empleado o cliente?: "))
            if opcion1== 1:
                self.mostrar_menu21()
                opcion21 = int(input("Seleccione una opción: "))
                if opcion21==1:
                    mi_auto=Auto(None,None,None,None)
                    mi_auto.informacion_autos()
                elif opcion21==2:
                    mi_concesionaria=Concesionaria()
                    mi_concesionaria.crear_auto()
                elif opcion21==3:
                    Auto.modificar_auto()
                elif opcion21==4:
                    Venta.informacion_ventas()
                elif opcion21==5:
                    Venta.modificar_venta()
                elif opcion21==6:
                    Cliente.informacion_clientes()
                elif opcion21==7:
                    Cliente.modificar_cliente()
                elif opcion21==8:
                    self.salir()
                else:
                    print(f"{opcion1} no es una opción válida")
            elif opcion1==2:
                self.mostrar_menu22()
                opcion22 = int(input("Seleccione una opción: "))
                if opcion22==1:
                    pass
                elif opcion22==2:
                    mi_auto=Auto(None,None,None,None)
                    mi_auto.informacion_autos()
                elif opcion22==3:
                    Auto.busqueda_auto()
                elif opcion22==4:
                    mi_concesionaria=Concesionaria()
                    mi_concesionaria.registrar_cliente()
                else:
                    print(f"{opcion1} no es una opción válida")
            else:
                print(f"{opcion1} no es una opción válida")

    def salir(self):
        print("\nGRACIAS CONFIAR EN NOSOTROS. VUELVA PRONTO")
        sys.exit(0)