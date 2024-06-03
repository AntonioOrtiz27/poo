import abc
from abc import ABC

class Servicio(ABC):
    __nomE:str
    __nomC:str
    __direccionC:str
    __fecha:str
    __comision:float
        
    
    def __init__(self, Nome, NomC, Direccion, Fecha, Comision):
        self.__nomE = Nome
        self.__nomC = NomC
        self.__direccionC = Direccion
        self.__fecha = Fecha
        self.__comision = Comision
        
    def __str__(self):
        return f"{self.__nomE} {self.__nomC} {self.__direccionC} {self.__fecha} {self.__comision}"

    def getNomC(self):
        return self.__nomC
    def getComision(self):
        return self.__comision
    def getFecha(self):
        return self.__fecha
    
    @abc.abstractmethod
    def Costito(self):
        pass
        