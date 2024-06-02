from gestorCancha import *
from gestorAlquiler import *


def test():
    op=int(input("""
        [0]: para salir.
        [1]: Carga de Canchas.
        [2]: Carga de Alquiler.
        [3]: inciso B.
        [4]: inciso A.
    """))
    return op

if __name__=="__main__":
    GC=gestor_cancha()
    GA=gestor_alquiler()
    GC.cargarCancha()
    GA.cargarAlquiler()

    opcion=test()
    while opcion!=0:
        if opcion==1:
            GC.mostrar1()
        elif opcion==2:
            GA.mostrar2()
        elif opcion==3:
            ide=str(input("ingerese una cancha:"))
            GC.minutitos(ide,GA)
        elif opcion==4:
            print(" listado ordenado de los alquileres registrados por hora y minutos.")
            GA.listado(GC)
            
            
        opcion=test()

