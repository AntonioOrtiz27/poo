from gestorlista import *
from gestorNP import *

def menu():
      op = int(input("""Ingrese opcion:
                     1_cargar mamas
                     2_cargar Nacimientos
                     3_Ingrese un dni
                     4_parto múltiple
                     0_Para finalizar\n"""))
      return op


if __name__=='__main__':
    GN = gestor_lista() #asigno la clase
    GN.cargarcsvlista()
    GM = gestor_numpy() #asigno la clase
    GM.cargarcsv()
    
    #menu:
    opcion = menu()
    while opcion!=0:
        if opcion == 1:
            GM.mostrar_arreglo()
        elif opcion == 2:
            GN.mostrar_lista() 
        elif opcion == 3:
            dni=str(input("ingrese un dni:"))
            GM.mostrar_listado(dni,GN)
        elif opcion == 4:
            GN.mostrar_Mas_de_unNac(GM)
        else: 
            print("Numero ingresado no corresponde\n")
        opcion = menu()