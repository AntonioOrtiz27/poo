class transaccion:
    __cvu:str
    __numT:int
    __importe:float
    __tipo:str
    
    def __init__(self,Cvu,NumT,Importe:float,Tipo):
        self.__cvu=Cvu
        self.__numT=NumT
        self.__importe=Importe
        self.__tipo=Tipo
    
    def get_cvu(self):
        return self.__cvu
    
    def get_numT(self):
        return int(self.__numT)
    
    def get_importe(self):
        return float(self.__importe)
    
    def get_tipo(self):
        return self.__tipo
    
    def __str__(self):
        return f"Cvu: {self.__cvu} NumT: {self.__numT} Importe: {self.__importe} Tipo: {self.__tipo}"