import abc
from abc import ABC

class Producto(ABC):
    __nombre: str
    __fechaE: str
    __fechaV: str
    __temperatura: float
    __pais: str
    __numLote: int
    __costo: float
    
    def __init__(self,Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo):
        self.__nombre = Nombre
        self.__fechaE = FechaE
        self.__fechaV = FechaV
        self.__temperatura = Temperatura
        self.__pais = Pais
        self.__numLote = NumLote
        self.__costo = Costo 
        
    def __str__(self):
        return f" {self.__nombre} {self.__fechaE} {self.__fechaV} {self.__temperatura} {self.__pais} {self.__numLote} {self.__costo} "
    def getNombre(self):
        return self.__nombre
    def getTemperatura(self):
        return self.__temperatura
    def getPais(self):
        return self.__pais
    def getCosto(self):
        return self.__costo
    def getFechavencimiento(self):
        return self.__fechaV

    
    @abc.abstractmethod
    def importe(self):
        pass
    