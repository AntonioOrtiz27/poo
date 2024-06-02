from calefactor import *

class Nodo:
    def __init__(self, calefactor) -> None:
        self.calefactor = calefactor
        self.siguiente = None
        
class Lista:
    def __init__(self):
        self.comienzo = None
        self.actual = None
        self.tope = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.actual is None:
            self.actual = self.comienzo
            raise StopIteration
        else:
            dato = self.actual.calefactor
            self.actual = self.actual.siguiente
            return dato

    def to_dict(self):
        d = dict(
            __class__=self.__class__.__name__,
            calefactores=[calefactor.to_dict() for calefactor in self]
            )
        return d
    
    def agregar(self, calefactor):
        nodo = Nodo(calefactor)
        nodo.siguiente = self.comienzo
        self.comienzo = nodo
        self.actual = self.comienzo
        self.tope += 1
        
    def insertar(self, calefactor, indice):
        if indice >= 0 and indice < self.tope:
            aux = self.comienzo
            for _ in range(indice - 2):
                aux = aux.siguiente
                
            nodo = Nodo(calefactor)
            nodo.siguiente = aux.siguiente
            aux.siguiente = nodo
            return
        else:
            raise IndexError("Posicion no valida")
        
    def mostrar_tipo(self, indice):
        if indice >= 0 and indice < self.tope:
            aux = self.comienzo
            for _ in range(indice - 1):
                aux = aux.siguiente 
            if isinstance(aux.calefactor, CalefactorElectrico):
                print("Calefactor Electrico")
            else:
                print("Calefactor a Gas")
        else:
            raise IndexError("Posicion no valida")
 #???????????????
        
    def mostrar_mejor(self):
        mejor_calefactor = self.comienzo.calefactor
        for calefactor in self:
            if isinstance(calefactor, CalefactorGas):
                if calefactor.precio < mejor_calefactor.precio:
                    mejor_calefactor = calefactor
                    
        print(mejor_calefactor)
        
    
    def mostrar_marca(self, marca):
        for calefactor in self:
            if isinstance(calefactor, CalefactorElectrico) and calefactor.marca == marca:
                print(calefactor.modelo, calefactor.potencia, calefactor.precio)
    
    def mostrar_promociones(self):
        for calefactor in self:
            if calefactor.promocion == "Si":
                print(calefactor.marca, calefactor.modelo, calefactor.pais, calefactor.calcular_importe())