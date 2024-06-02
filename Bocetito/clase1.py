class  :
    __variable1: str
    __variable2: str 
    __variable3: int
    __variable4: int 
    __variable5: str
    
    def __init__(self,v11,v22,v33,v44,v55):
        self.__variable1 = v11
        self.__variable2 = v22
        self.__variable3 = v33
        self.__variable4 = v44
        self.__variable5 = v55    
        
    def __str__(self):
        return f"variable1:{self.__variable1}variable2:{self.__variable2}variable3:{self.__variable3} variable4:{self.__variable4} variable5:{self.__variable5}\n"
    
    def getv11(self):
        return self.__variable1
    
    def getv22(self):
        return self.__variable2
    
    def getv33(self):
        return self.__variable3
    
    def getv44(self):
        return self.__variable4
    
    def getv55(self):
        return self.__variable5


