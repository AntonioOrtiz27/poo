from claseCongelados import *
from claseRefrigerados import *
from claseProductos import *
from gestorProductos import gestor_Productos

def test():
    try:    
        opcion = int(input("""
                            Menu de opciones
            Ingrese opcion: 
            1_Cargar Productos
            2_
            3_
            4_
            5_
            6_
            0_Para finalizar
            ----->""")) 
    except ValueError:
        print(f"Ingrese un valor numerico del menú de opciones.")
    return opcion 
        
if __name__ == '__main__':
    lista = gestor_Productos()
    lista.cargar_Csv()

    op=test()
    while op != 0:
        if op == 1:
            lista.mostrararchi()
        elif op == 2:
            try:
                dato=int(input("Ingrese el tipo a insertar en la lista de Productos: [1]Congelados [2]Refrigrados [0] salir):"))
                if dato == 1:
                    Nombre=input("ingrese Nombre:")
                    FechaE=input("ingrese Fecha envasado:")
                    FechaV=input("ingrese fecha vencimiento:")
                    Temperatura=float(input("ingrese temperatura:"))
                    Pais=str(input("ingrese pais:"))
                    NumLote=int(input("ingrese num lote:"))
                    Costo=float(input("ingrese costo:"))
                    Nitrogeno=float(input("ingrese Nitrogeno:"))
                    Oxigeno=float(input("ingrese oxigeno:"))
                    Dioxido=float(input("ingrese dioxido:"))
                    Vapor=float(input("ingrese vapor:"))
                    Metodo=str(input("ingrese metodo:"))
                    objetito= Congelado(Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo,Nitrogeno,Oxigeno,Dioxido,Vapor,Metodo)
                    lista.agregarproductos(objetito)
                elif dato == 2:
                    Nombre=input("ingrese Nombre d:")
                    FechaE=input("ingrese Fecha envasado:")
                    FechaV=input("ingrese fecha vencimiento:")
                    Temperatura=float(input("ingrese temperatura:"))
                    Pais=str(input("ingrese pais:"))
                    NumLote=int(input("ingrese num lote:"))
                    Costo=float(input("ingrese costo:"))
                    Codigo=int(input("ingrese codigo:"))
                    objetito= Refrigerado(Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo,Codigo)
                    lista.agregar_producto(objetito)
                else:
                    print("Opción de servicio no válida.")
            except ValueError:
                print(f"Coloca un servicio que sea 1 o 2.")
        elif op==3:
            lista.mostrar_agregados()
        elif op == 4:
            pos=int(input("ingrse posicion:"))
            lista.almacenado(pos)
        elif op == 5:
            lista.cantidad()
        elif op ==6:
            lista.recorrer()
        op=test()
        