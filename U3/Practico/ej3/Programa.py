class Programa :
    __nom: str
    __cod: str 
    __duracion: int
    __listamatricula:list
    
    def __init__(self,Nom,Cod,Dur:int):
        self.__nom = Nom
        self.__cod = Cod
        self.__duracion = Dur   
        self.__listamatricula = []
        
    def __str__(self):
        return f"nom:{self.__nom}cod:{self.__cod}duracion:{self.__duracion}\n"
    
    def getNom(self):
        return self.__nom
    
    def getCodigo(self):
        return self.__cod
    
    def getDuracion(self):
        return self.__duracion
    
    def addMatricula(self,matricula):
        self.__listamatricula.append(matricula)
    
