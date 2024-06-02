from claseNodo import Nodo
from claseDepartamento import Departamento
from claseCasa import Casa
from claseInmuebles import Inmueble

class Lista:
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0 
        
    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0  # Reset index at the start of iteration
        return self
    
    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        else:
            datito = self.__actual.getInmueble()
            self.__actual = self.__actual.siguiente
            self.__indice += 1
            return datito
        
    def insertar(self, pos: int, dato: Inmueble):
        nodo = Nodo(dato)
        if self.__comienzo is None or pos == 0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            contador = 0
            while contador < pos - 1 and aux.siguiente is not None:
                aux = aux.siguiente
                contador += 1
            nodo.setSiguiente(aux.siguiente)
            aux.setSiguiente(nodo)
        self.__tope += 1
        
    def agregar_uno(self, elemento: Inmueble):
        nodo = Nodo(elemento)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.setSiguiente(nodo)
        self.__tope += 1
        print("Inmueble cargado al final de la lista.\n")
        
    def total(self, cantidad):
        for listita in self:
            if isinstance(listita, Departamento) and listita.getCantidad() < cantidad:
                importesito = listita.calculo()
                print(f"Datos:\n{listita}\n importe:{importesito}\n")
            elif isinstance(listita, Departamento): 
                print("\nEl Dpto actual tiene igual o más dormitorios.\n")


