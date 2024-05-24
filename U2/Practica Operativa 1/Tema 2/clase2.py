class Cliente:
    __Nombre: int
    __apellido: str 
    __dni: str
    __numCuenta: int 
    __saldoAnterior: float
    
    def __init__(self,Nombre,Apellido,Dni,Numcuenta,Saldo):
        self.__Nombre = Nombre
        self.__apellido = Apellido
        self.__dni = Dni
        self.__numCuenta = int(Numcuenta)
        self.__saldoAnterior = float(Saldo)   
        
    def __str__(self):
        return f"Nombre:{self.__Nombre} apellido:{self.__apellido} dni:{self.__dni} numCuenta:{self.__numCuenta} saldoAnterior:{self.__saldoAnterior}\n"
    
    def getNombre(self):
        return self.__Nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDni(self):
        return self.__dni
    
    def getNumcuenta(self):
        return int(self.__numCuenta)
    
    def getSaldo(self):
        return self.__saldoAnterior
    
    def SetSaldo(self,Saldo):
        self.__saldoAnterior = Saldo