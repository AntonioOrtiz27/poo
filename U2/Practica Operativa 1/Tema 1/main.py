from GestorClientes import *
from GestorMovimientos import *
from ClaseMovimientos import Movimiento

def menu():
    print(""" 1. Estado del Cliente del DNI a ingresar
    2. Movimientos Abril 2024
    3. Ordenar Movimientos 
    0. Salir""")
    
if __name__=="__main__":    
    GC=GestorClientes()
    GC.csvCliente()

    GM=GestorMovimientos()
    GM.csvMovimientos()    
    
    opcion=menu()
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        if opcion == 1:
            GC.BuscarDNI(GM)
        elif opcion == 2:
            GC.nomyape(GM)
        elif opcion == 3:
            GM.OrdenarMovimientos()
            print("Movimientos Ordenados")
            GM.mostrar_arreglo()
        opcion = int(input("Ingrese una opcion: "))
        