class  Nacimiento:
    __dni: str
    __tipo: str 
    __fecha: str
    __hora: str
    __peso: float
    __altura:int
    
    def __init__(self,Dni,Tipo,Fecha,Hora,Peso:float,Altura:int):
        self.__dni = Dni
        self.__tipo = Tipo
        self.__fecha = Fecha
        self.__hora = Hora
        self.__peso = Peso
        self.__altura= Altura
        
    def __str__(self):
        return f"dni:{self.__dni}tipo:{self.__tipo}fecha:{self.__fecha} hora:{self.__hora} peso:{self.__peso} Altura:{self.__altura}\n"
    
    def getDni(self):
        return self.__dni
    
    def getTipo(self):
        return self.__tipo
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura
    
    def __eq__(self, otro):
        return self.__dni == otro.getDni()  and self.__fecha == otro.getFecha() 