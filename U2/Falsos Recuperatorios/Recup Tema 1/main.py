from gestorReserva import *
from gestorCabañas import *

def menu():
      op = int(input("""Ingrese opcion:
                     1_cargar Cabaña
                     2_cargar Reserva
                     3_
                     4_
                     0_Para finalizar\n"""))
      return op


if __name__=='__main__':
    GC = gestor_cabaña() #asigno la clase
    GC.cargarcsv()
    GR = gestor_reserva() #asigno la clase
    GR.cargarcsvlista()    
    #menu:
    opcion = menu()
    while opcion!=0:
        if opcion == 1:
            GC.mostrar_arreglo() 
        elif opcion == 2:
            GR.mostrar_lista()
        elif opcion == 3:
            GC.mostrarNumC(GR)
        elif opcion == 4:
            GR.listar(GC)
        else: 
            print("Numero ingresado no corresponde\n")
        opcion = menu()