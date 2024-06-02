from claseProductos import Producto

class Congelado(Producto):
    __nitro:float;
    __oxig:float
    __diox:float
    __vapor:float
    __metodo:str
    
    def __init__(self,Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo,Nitrogeno,Oxigeno,Dioxido,Vapor,Metodo):
        super().__init__(Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo)
        self.__nitro = Nitrogeno
        self.__oxig = Oxigeno
        self.__diox = Dioxido
        self.__vapor = Vapor
        self.__metodo = Metodo
    
    def __str__(self):
        return super().__str__() + f"{self.__nitro} {self.__oxig} {self.__diox} {self.__vapor} {self.__metodo}"
    
    def getMetodo(self):
        return self.__metodo
    
    def importe(self):
        imp:float=0.0
        if self.__metodo=="mecanico":
            imp += super().getCosto()+15.01
        elif self.__metodo=="criogenico":
            imp += super().getCosto()+15.01
        return imp
