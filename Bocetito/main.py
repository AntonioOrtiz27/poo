from gestorlista import *
from gestorNP import *

def menu():
      op = int(input("""Ingrese opcion:
                     1_cargar
                     2_cargar
                     3_
                     4_
                     0_Para finalizar\n"""))
      return op


if __name__=='__main__':
    GX = gestor_lista() #asigno la clase
    GX.cargarcsvlista()
    GX.mostrar_lista() 
    GY = gestor_numpy() #asigno la clase
    GY.cargarcsv()
    GY.mostrar_arreglo()
    
    #menu:
    opcion = menu()
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    else: 
        print("Numero ingresado no corresponde\n")
    opcion = menu()