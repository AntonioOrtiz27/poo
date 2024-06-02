class cancha:
    __id:str
    __tipo:int
    __imp:float

    def __init__(self,idd,Tipo,importe:float):
        self.__id=idd
        self.__tipo=Tipo
        self.__imp=float(importe)

    def __str__(self):
        return f"id:{self.__id} Tipo:{self.__tipo} Importe:{self.__imp}\n"

    def getid(self):
        return self.__id
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__imp