class Cabaña :
    __num: int
    __cantH: int
    __cantC: int
    __cantCC: int 
    __importe: int
    
    def __init__(self,Num,CantH,CantC,CantCC,Importe):
        self.__num = Num
        self.__cantH = CantH
        self.__cantC = int(CantC)
        self.__cantCC = int(CantCC)
        self.__importe = int(Importe)    
        
    def __str__(self):
        return f"num:{self.__num} cantC:{self.__cantC} cantH:{self.__cantH} cantCC:{self.__cantCC} importe:{self.__importe}\n"
    
    def getNum(self):
        return self.__num
    
    def getCantH(self):
        return self.__cantH
    
    def getCantC(self):
        return self.__cantC
    
    def getCantCC(self):
        return self.__cantCC
    
    def getImporte(self):
        return self.__importe
    
    def capacidad(self):
        return self.__cantC*2 + self.__cantCC
    
    def __ge__(self, other):
        if isinstance(other, int):
            return self.capacidad() >= other

