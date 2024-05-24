from gestorlista2 import *
from gestorlista1 import *
from gestorlista3 import *

def menu():
      op = int(input("""Ingrese opcion:
                     1_cargar empleados
                     2_cargar programa
                     3_cargar matricula
                     4_"Duración de todos los programas decapacitación en los que está matriculado."
                     0_Para finalizar\n"""))
      return op


if __name__=='__main__':
    GE = gestor_lista_1() #asigno la clase
    GE.cargarcsvlista()
    GP = gestor_lista_2() #asigno la clase
    GP.cargarcsvlista_2()
    GM = gestor_lista_3() #asigno la clase
    GM.cargarcsvlista_3(GE,GP)
    
    #menu:
    opcion = menu()
    while opcion!= 0:
        if opcion == 1:
            GE.mostrar_lista() 
        elif opcion == 2:
            GP.mostrar_lista_2()
        elif opcion == 3:
            GM.mostrar_lista_3()
        elif opcion == 4:
            idd=int(input("Ingrese id de un empleadinho:"))
            GE.obtenerId(idd)
        else: 
            print("Numero ingresado no corresponde\n")
        opcion = menu()