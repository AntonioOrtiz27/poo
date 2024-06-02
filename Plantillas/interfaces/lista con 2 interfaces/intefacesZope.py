from lista import Lista   
from interfaces import ICajero, ISupervisor

def mostrar_menu_cajero():
    print("\nMenú de opciones:")
    print("1. Mostrar elementos")
    print("2. Buscar elemento")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def mostrar_menu_supervisor():
    print("\nMenú de opciones:")
    print("1. Agregar elemento")
    print("2. Insertar elemento en una posición")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def cajero(lista):
    continuar = True
    while continuar:
        opcion = mostrar_menu_cajero()
        
        if opcion == 1:
            lista.mostrar()
        
        elif opcion == 2:
            dato = int(input("Ingrese el dato a buscar: "))
            indice = lista.buscar(dato)
            if indice != -1:
                print(f"El dato {dato} se encuentra en la posición {indice + 1}.")
            else:
                print(f"El dato {dato} no se encuentra en la lista.")
        
        elif opcion == 3:
            print("Saliendo...")
            continuar = False
         
        else:
            print("Opción no válida. Intente de nuevo.")
        
        
def supervisor(lista):
    continuar = True
    while continuar:
        opcion = mostrar_menu_supervisor()
    
        if opcion == 1:
            dato = input("Ingrese el dato a agregar: ")
            lista.agregar(dato)
        
        elif opcion == 2:
            posicion = int(input("Ingrese la posición donde insertar: "))
            dato = input("Ingrese el dato a insertar: ")
            try:
                lista.insertar(posicion - 1, dato)
            except IndexError as e:
                print(e)
        
        elif opcion == 3:
            print("Saliendo...")
            continuar = False
         
        else:
            print("Opción no válida. Intente de nuevo.")
        
        
def testInterfaces():
    lista = Lista()
    for i in range(5):
        lista.agregar(i)
    
    usuario = input('Usuario (Admin/Cajero): ')
    clave = input('Clave:')
    if usuario.lower() == 'admin' and clave == 'a54321':
        supervisor(ISupervisor(lista))
    elif usuario.lower() == 'cajero' and clave == 'c12345':
        cajero(ICajero(lista))
            
            
if __name__=='__main__':
    testInterfaces()