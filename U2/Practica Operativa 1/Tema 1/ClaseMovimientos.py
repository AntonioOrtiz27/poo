class Movimiento:
    __numTarjeta:str
    __fecha:str
    __descripcion:str
    __TipoMov:str
    __importe:float
    
    def __init__(self,NumTarjeta:str,Fecha:str,Descripcion:str,tipoMov:str,Importe:float):
        self.__numTarjeta=NumTarjeta
        self.__fecha=Fecha
        self.__descripcion=Descripcion
        self.__TipoMov=tipoMov
        self.__importe=Importe    
        
    def __str__(self):
        return f"Numero de tarjeta:{self.__numTarjeta} Fecha:{self.__fecha} descripcion:{self.__descripcion} tipo movimiento:{self.__TipoMov} importe:{self.__importe}"
    
    def get_NumTarjeta(self):
        return self.__numTarjeta
    
    def get_Fecha(self):
        return self.__fecha
    
    def get_Descripcion(self):
        return self.__descripcion
    
    def get_tipoMov(self):
        return self.__TipoMov
    
    def get_Importe(self):
        return self.__importe
    
    def __lt__(self, otro):
        return self.__numTarjeta < otro.__numTarjeta
    