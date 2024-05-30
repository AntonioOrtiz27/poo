from claseServicio import Servicio

class ServicioE(Servicio):
    __precio:float
    __peso:float
    __cantidad:int
    
    def __init__(self, Nome, NomC, Direccion, Fecha, Comision,Precio,Peso,Cantidad):
        super().__init__(Nome, NomC, Direccion, Fecha, Comision)
        self.__precio=Precio
        self.__peso=Peso
        self.__cantidad=Cantidad   
        
    def __str__(self):
        return super().__str__() + f"{self.__precio} {self.__peso} {self.__cantidad} "
    
    def getPesito(self): 
        return self.__peso
    
    def getPrice(self):
        return self.__precio
    
    def Costito(self):
        if self.__peso > 50:
            costo = super().Comision + ((self.__Precio * self.__Cantidad) + (0.1 * self.__Peso)) 
        else:
            costo = super().Comision + (self.__Precio * self.__Cantidad)
        return costo
    

    

    