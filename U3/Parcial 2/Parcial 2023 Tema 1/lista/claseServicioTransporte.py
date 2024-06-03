from claseServicio import Servicio

class ServicioT(Servicio):
    __precio:float
    __peso:float
    __direccionDestino:str
    __hora:float
    
    def __init__(self, Nome, NomC, Direccion, Fecha, Comision,Precio,Peso,DireccionDestino,Hora):
        super().__init__(Nome, NomC, Direccion, Fecha, Comision)
        self.__precio=Precio
        self.__peso=Peso
        self.__direccionDestino=DireccionDestino    
        self.__hora=Hora
        
    def __str__(self):
        return super().__str__() + f"{self.__precio} {self.__peso} {self.__direccionDestino} {self.__hora}"
    
    def getPeso(self):
        return self.__peso
    
    def getPrecio(self):
        return self.__precio
    
    def Costito(self):
        if self.__peso > 500:
            return self.__precio*self.__hora*10
        else:
            return self.__precio*self.__hora
        