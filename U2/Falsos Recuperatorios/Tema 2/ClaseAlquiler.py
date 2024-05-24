class Alquiler:
    __nom:str
    __id:str
    __hora:str
    __minutos:str
    __duracion:int

    def __init__(self,Nom,idd,Hora,Minutos,Duracion:int):
        self.__nom=Nom
        self.__id=idd
        self.__hora=Hora
        self.__minutos=Minutos
        self.__duracion=int(Duracion)

    def __str__(self):
        return f"nombre:{self.__nom} id:{self.__id} hora:{self.__hora} minutos:{self.__minutos} duracion:{self.__duracion}\n"

    def getNom(self):
        return self.__nom
    
    def getID(self):
        return self.__id
    
    def getHora(self):
        return self.__hora
    
    def getMinutos(self):
        return self.__minutos

    def getDuracion(self):
        return self.__duracion
    
    def __gt__(self,other):
        if self.__hora == other.getHora():
            return self.__minutos > other.getMinutos()
        else:
            return self.__hora > other.getHora()