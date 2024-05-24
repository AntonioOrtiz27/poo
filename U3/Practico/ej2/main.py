from GestorMaterial import *
from GestorLadrillos import *

def menu():
    op = int(input("""Ingrese una opcion
                    [0] : Para Salir
                    [1] : Mostrar Ladrillos
                    [2] : Mostrar Material
                    [3] : costo Total y característica del material solicitado. 
                    [4] : mostrar el detalle asociado con el formato.
                    ---------------------------------------------------->"""))
    return op

def testComposicion():
    GL = gestor_ladrillos()
    GM = gestor_material()
    GM.cargarMaterialesDesdeCSV()
    GL.cargarLadrillosDesdeCSV(GM)
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            GL.mostrar_Ladrillito()
        elif opcion == 2:
            GM.mostrar_material()
        elif opcion == 3:
            id=int(input("ingrese identificador:"))
            GL.caracterisitcas(GM,id)
        elif opcion == 4:
            GL.formato(GM)
        opcion = menu()
    
if __name__ == "__main__":
    testComposicion()
