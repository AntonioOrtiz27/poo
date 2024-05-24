class Empleado:
    __nya: str
    __idd: int 
    __puesto: str
    __matricula: list

    
    def __init__(self,Nya,Id,puesto):
        self.__nya = Nya
        self.__idd = Id
        self.__puesto = puesto
        self.__matricula =[]
        
    def __str__(self):
        return f"nya:{self.__nya}idd:{self.__idd}puesto:{self.__puesto}\n"
    
    def getNya(self):
        return self.__nya
    
    def getId(self):
        return self.__idd
    
    def getpuesto(self):
        return self.__puesto
    
    def getMatricula(self):
        return self.__matricula
    
    def addMatricula(self,matricula):
        self.__matricula.append(matricula)



