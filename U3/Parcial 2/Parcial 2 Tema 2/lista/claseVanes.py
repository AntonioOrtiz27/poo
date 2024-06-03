from claseVehiculo import Vehiculo

class Vanes(Vehiculo):
    __tipo:str
    
    def __init__(self,Marca, Modelo, Ano,Capacidad, Numero, Distancia, Tarifa,Tipo):
        super().__init__(Marca, Modelo, Ano,Capacidad, Numero, Distancia, Tarifa)
        self.__tipo = Tipo
    
    def __str__(self):
        return super().__str__() + f"{self.__tipo}" 
    
    def tarifa(self):
        imp:float=super().getTarifa()
        if self.__tipo=="minivan":
            imp -= imp*10/100
        else:
            imp = imp + (imp*2.5/100)
        return imp