class clientes:
    __nombre:str
    __apellido:str
    __dni:str
    __numtarjeta:str
    __saldo:float
    
    def __init__(self, Nombre:str , Apellido:str , Dni:str , NumTarjeta:int ,Saldo:float):
        self.__nombre= Nombre
        self.__apellido= Apellido
        self.__dni = Dni
        self.__numtarjeta= NumTarjeta
        self.__saldo= Saldo
        
    def __str__(self):
        return f"Nombre:{self.__nombre} Apellido:{self.__apellido} dni:{self.__dni} Numero de Tarjeta:{self.__numtarjeta} Saldo Anterior:{self.__saldo}"
    
    def get_Nombre(self):
        return self.__nombre
    
    def get_Apellido(self):
        return self.__apellido
    
    def get_DNI(self):
        return self.__dni
    
    def get_NumTarjeta(self):
        return self.__numtarjeta
    
    def get_Saldo(self):
        return self.__saldo
    
    def setSaldo(self,x):
        self.__saldo = x
    