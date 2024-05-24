class  Mamas:
    __dni: str
    __edad: int 
    __nya:str
    
    def __init__(self,Dni,Edad,Nya):
        self.__dni = Dni
        self.__edad = Edad
        self.__nya = Nya   
        
    def __str__(self):
        return f"dni:{self.__dni}edad:{self.__edad}Nombre y apellido: {self.__nya}\n"
    
    def getDni(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getNya(self):
        return self.__nya
    



