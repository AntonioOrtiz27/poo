import abc
from abc import ABC

class Vehiculo(ABC):
    __marca: str
    __modelo: str
    __ano: int
    __capacidad:int
    __numero: int
    __distancia: float
    __tarifa: float
    
    def __init__(self, Marca, Modelo, Ano,Capacidad, Numero, Distancia, Tarifa):
        self.__marca = Marca
        self.__modelo = Modelo
        self.__ano = Ano
        self.__capacidad=Capacidad
        self.__numero = Numero
        self.__distancia = Distancia
        self.__tarifa = Tarifa
        
    def __str__(self):
        return f"{self.__marca} {self.__modelo} {self.__ano} {self.__numero} {self.__distancia} {self.__tarifa}"
    
    @abc.abstractmethod
    def tarifa(self):
        pass
        
    def getModelo(self):
        return self.__modelo

    def getAno(self):
        return self.__ano
    
    def getCapacidad(self):
        return self.__capacidad
    def getTarifa(self):
        return self.__tarifa