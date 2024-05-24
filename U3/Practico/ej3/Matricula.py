class Matricula :
    __fecha: str
    __empleado: None
    __programa: None

    
    def __init__(self,Fecha,Emp:object,Programa:object):
        self.__fecha = Fecha
        self.__empleado = Emp
        self.__programa = Programa
        if Emp != None:
            self.__empleado.addMatricula(self)
        if Programa!= None:
            self.__programa.addMatricula(self)
        
    def __str__(self):
        if self.__programa != None and self.__empleado != None:
            return f"{self.__fecha} {self.__empleado.getNya()} {self.__programa.getNom()}\n"
        elif self.__empleado != None:
            return f"{self.__fecha} {self.__empleado.getNya()}\n"
        else:
            return f"{self.__fecha}"
    
    def getFecha(self):
        return self.__fecha
    
    def getEmpleado(self):
        return self.__empleado
    
    def getPrograma(self):
        return self.__programa
