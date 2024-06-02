class Reserva:
    __num: int
    __nom: str 
    __numC: int
    __fechaI: str
    __cantH: int
    __cantd:int
    __importe:float
    
    def __init__(self,Num,Nom,NumC,FechaI,CantH,CantD,Importe):
        self.__num = Num
        self.__nom = Nom
        self.__numC = NumC
        self.__fechaI = FechaI
        self.__cantH = CantH    
        self.__cantd= CantD
        self.__importe= Importe
        
    def __str__(self):
        return f"num:{self.__num} nom:{self.__nom} numC:{self.__numC} fechaI:{self.__fechaI} cantH:{self.__cantH} Cantidad Dias:{self.__cantd} importe:{self.__importe} \n"
    
    def getNum(self):
        return self.__num
    
    def getNom(self):
        return self.__nom
    
    def getNumc(self):
        return self.__numC
    
    def getFechai(self):
        return self.__fechaI
    
    def getCanth(self):
        return self.__cantH
    
    def getCantd(self):
        return self.__cantd
    
    def getImporte(self):
        return self.__importe
    
