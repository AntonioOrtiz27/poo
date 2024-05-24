from gestorMoto import *
from gestorPedido import *

def main():
    op=int(input("""
                 [0] Salir
                 [1] Cargar Motos
                 [2] Agregar Pedidos
                 [3] Verificar si la moto existe.
                 [4] Actualizar Tiempo Real del pedido 
                 [5] Tiempo promedio real de entrega de los pedidos que hizo. 
                 [6] Listado
                 [7] Ordenar de menor a mayor por numero de patente los Pedidos.
                 """))
    return op

if __name__ == "__main__":
    GM=gestor_motos()
    GP=gestor_pedidos()
    GM.cargar_Csv_Motos()
    GP.cargar_Csv_Pedidos()
    
    opcion=main()
    while opcion!=0:
        if opcion==1:
            GM.cargar_Csv_Motos()
            GM.mostrar_motos()
        elif opcion==2:
            GP.cargar_Csv_Pedidos()
            GP.mostrar_pedidos()
        elif opcion==3:
            patente=str(input("Ingrese la patente: "))
            GP.verificar(GM,patente)
        elif opcion == 4:
            pat = input("Ingrese la patente: ")
            idd = int(input("Ingrese el id del pedido: "))
            Tr = int(input("Ingrese el tiempo real de entrega: "))
            GP.actualizar(pat, idd, Tr)
        elif opcion==5:
            GP.nyaConductor(GM)
        elif opcion==6:
            GM.verificarpatente(GP)
        elif opcion==7:
            GP.ordenar()
        opcion=main()
