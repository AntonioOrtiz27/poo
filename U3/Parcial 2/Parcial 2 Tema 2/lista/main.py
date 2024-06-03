from claseAutobus import *
from claseVanes import *
from claseVehiculo import *
from gestorVehiculo import gestor_Vehiculo

def test():
    try:    
        opcion = int(input("""
                            Menu de opciones
            Ingrese opcion: 
            1_cargar csv
            2_Agregar vehiculos
            3_Mostrar el vehiculo agregado en la lista.
            4_Buscar un vehiculo por posicion.
            5_Cantidad de vehiculos de cada tipo.
            6_Mostrar modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio.
            0_Para finalizar
            ----->""")) 
    except ValueError:
        print(f"Ingrese un valor numerico del menú de opciones.")
    return opcion 
        
if __name__ == '__main__':
    lista = gestor_Vehiculo()
    lista.cargarcsv()
    
      
    #insertar por posición Manuel,al final pos-1 o a la cabeza pos.
    op=test()
    while op != 0:
        if op == 1:
            lista.mostrarcsv()
        elif op==2:
            try: 
                tipo=int(input("ingrese el tipo de vehiculo a agregar:\n [0] Salir. \n [1] Autobuses.\n [2] Vanes\n--->"))
                if tipo == 1:
                    Marca=input("ingrese marquinha:")
                    Modelo=input("ingrese modelinho:")
                    Ano=int(input("ingrese ano:"))
                    Capacidad=int(input("ingrese capacidad:"))
                    Numero=int(input("ingrese numerinho de plazinhas"))
                    Distancia=float(input("ingrese distancinha:"))
                    Tarifa=int(input("ingrese tarifinha:"))
                    Tipo=input("ingrese tipo de servicio(interurbano, turismo:")
                    Turno=input("ingrese turno (mañana, tarde, noche:")
                    objetinho=Autobuses(Marca, Modelo, Ano,Capacidad ,Numero, Distancia, Tarifa,Tipo,Turno)
                    lista.agregar(objetinho)
                elif tipo == 2:
                    Marca=input("ingrese marquinha:")
                    Modelo=input("ingrese modelinho:")
                    Ano=int(input("ingrese ano:"))
                    Capacidad=int(input("ingrese capacidad:"))
                    Numero=int(input("ingrese numerinho de plazinhas"))
                    Distancia=float(input("ingrese distancinha:"))
                    Tarifa=int(input("ingrese tarifinha:"))
                    Tipo=input("ingrese el tipo de carrocería (minivan, van):")
                    objetinho=Vanes(Marca, Modelo, Ano,Capacidad, Numero, Distancia, Tarifa,Tipo)
                    lista.agregar(objetinho)
                else:
                    print("opcion seleccionada no valida(1 o 2).")
            except ValueError:
                print("ingrese un valor que no sea una cadena(letras).")
        elif op==3:
            lista.mostrar_Agregado()
        elif op==4:
            pos=int(input("ingrese una posicion a buscar de un tipo de car:"))
            lista.buscar(pos)
        elif op==5:
            lista.cantidad()
        elif op == 6:
            lista.bytarifa()
        op=test()
        