from gestorlista import *
from gestorNP import *

def menu():
      op = int(input("""Ingrese opcion:
                     1_Mostrar clientes
                     2_Mostrar Movimientos
                     3_Actualiza el saldo
                     4_Clientes con movimientos en el mes de abril 2024
                     5_Ordenar por numero de cuenta
                     0_Para finalizar\n"""))
      return op


if __name__=='__main__':
    GC = gestor_lista() #asigno la clase
    GC.cargarcsv()
    GM = gestor_numpy() #asigno la clase
    GM.cargarcsv()
    
    #menu:
    opcion = menu()
    while opcion!= 0:
        if opcion == 1:
            GC.mostrar_lista() 
        elif opcion == 2:
            GM.mostrar_arreglo()
        elif opcion == 3:
            GC.dni(GM)
        elif opcion==4:
            GC.Tarjeta(GM)    
        elif opcion==5:
            GM.ordenar()
        opcion = menu()