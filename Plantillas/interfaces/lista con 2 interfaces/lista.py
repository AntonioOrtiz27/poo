from zope.interface import Interface
from zope.interface import implementer
from interfaces import ICajero, ISupervisor

class Nodo:
    __dato: object
    __siguiente: object

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def set_siguiente(self, dato):
        self.__siguiente = dato
    
    def get_dato(self):
        return self.__dato
    
    def get_siguiente(self):
        return self.__siguiente
    

@implementer(ICajero)
@implementer(ISupervisor)
class Lista:
    __cabeza: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__cabeza = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        self.__actual = self.__cabeza
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__indice = 0
            self.__actual = self.__cabeza
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
        
    def mostrar(self):
        print("Elementos de la lista:")
        for dato in self:
            print(dato)
        
    def agregar(self, dato):
        aux = self.__cabeza
        nodo = Nodo(dato)
        if aux != None:
            while aux.get_siguiente() != None:
                aux = aux.get_siguiente()
            aux.set_siguiente(nodo)
        else: 
            self.__cabeza = nodo
        self.__tope += 1
    
    def agregar_por_cabeza(self, dato):
        nodo = Nodo(dato)
        nodo.set_siguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__tope += 1
    
    def insertar(self, indice, dato):
        if self.__cabeza == None or indice == 0:
            nodo = Nodo(dato)
            nodo.set_siguiente(self.__cabeza)
            self.__cabeza = nodo
        elif 0 <= indice < self.__tope:
            aux = self.__cabeza
            for _ in range(indice - 1):
                aux = aux.get_siguiente()
            nodo = Nodo(dato)
            nodo.set_siguiente(aux.get_siguiente())
            aux.set_siguiente(nodo)
        else:
            raise IndexError("Posicion incorrecta")
        self.__tope += 1

    def buscar(self, dato):
        aux = self.__cabeza
        indice = 0
        while aux is not None:
            if aux.get_dato() == dato:
                return indice
            aux = aux.get_siguiente()
            indice += 1
        return -1
    
    def buscar_dato(self, indice):
        if 0 <= indice < self.__tope:
            aux = self.__cabeza
            for _ in range(indice):
                aux = aux.get_siguiente()
            return aux.get_dato()
        else:
            raise IndexError("Posicion incorrecta")


def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar elemento")
    print("2. Insertar elemento en una posición")
    print("3. Mostrar elementos")
    print("4. Buscar elemento por valor")
    print("5. Buscar elemento por índice")
    print("6. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


if __name__ == "__main__":
    lista = Lista()
    
    for i in range(5):
        lista.agregar(i)
    
    continuar = True
    while continuar:
        opcion = mostrar_menu()
    
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
            lista.mostrar()
        
        elif opcion == 4:
            dato = int(input("Ingrese el dato a buscar: "))
            indice = lista.buscar(dato)
            if indice != -1:
                print(f"El dato {dato} se encuentra en la posición {indice + 1}.")
            else:
                print(f"El dato {dato} no se encuentra en la lista.")
        
        elif opcion == 5:
            posicion = int(input("Ingrese la posicion del dato a buscar: "))
            try:
                dato = lista.buscar_dato(posicion - 1)
                print(f"El dato en la posición {posicion} es {dato}.")
            except IndexError as e:
                print(e)
        
        elif opcion == 6:
            print("Saliendo...")
            continuar = False
         
        else:
            print("Opción no válida. Intente de nuevo.")