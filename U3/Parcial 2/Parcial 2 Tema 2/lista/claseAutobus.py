from claseVehiculo import Vehiculo

class Autobuses(Vehiculo):
    __tipo:str
    __turno:str
    
    def __init__(self,Marca, Modelo, Ano,Capacidad ,Numero, Distancia, Tarifa,Tipo,Turno):
        super().__init__(Marca, Modelo, Ano,Capacidad, Numero, Distancia, Tarifa)
        self.__tipo= Tipo
        self.__turno=Turno   
        
    def __str__(self):
        return super().__str__() + f"{self.__tipo} {self.__turno}"
    
    def tarifa(self):
        imp:float=0
        if self.__turno=="nocturno" and self.__tipo=="turismo":
            imp += (super().getTarifa() + (super().getTarifa()*20/100))
        else:
            imp += (super().getTarifa() + (super().getTarifa()*5/100))
        return imp
    
