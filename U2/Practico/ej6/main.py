from GestorCuentas import *
from GestorTransacciones import *

def menu():
    op:int
    op=int(input("""
                 Menu de Opciones
                 [0] Salir
                 [1] Apellido, nombre,CVU y saldo (actualizado por las transacciones) del cliente.
                 [2] Modificar porcentaje anual
                 [3] actualizar saldo
                 [4] Saldo para la cuenta que es identificada por el CVU.
                 [5] Datos actualizados de las Cuentas
                 --->"""))
    return op

if __name__=="__main__": 
    GC=gestor_cuenta()
    GT=gestor_Transacciones()
    GC.csv_cuenta()
    GT.csv_transacciones()
    
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            dni=str(input("ingrese dni: "))
            GC.informar(dni,GT)
        elif opcion==2:
            pNuevo=float(input("ingrese porcentaje nuevo: "))
            GC.modificar(pNuevo)
        elif opcion==3:
            GC.actualiza()
        elif opcion==4:
            GC.saldoNuevo(GT)
        elif opcion==5:
            GC.cargar_Csv_Actualizado()
        opcion=menu()
    