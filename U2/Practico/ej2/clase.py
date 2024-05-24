class cuenta:
    __cuil: str
    __apellido: str 
    __nombre:str
    __saldo:float
    
    def __init__(self,Cuil,Apellido,Nombre,Saldo):
        self.__cuil = Cuil
        self.__apellido= Apellido
        self.__nombre = Nombre 
        self.__saldo = Saldo   
        
    def __str__(self):
        return f"Cuil:{self.__cuil} Apellido:{self.__apellido} Nombre: {self.__nombre} Saldo:{self.__saldo}\n"
    
    def ObtenerCuil(self):
        return self.__cuil
    
    def ObtenerApellido(self):
        return self.__apellido
    
    def ObtenerNombre(self):
        return self.__nombre
        
    def ObtenerSaldo(self):
        return self.__saldo

    