class cuenta:
    __nya:str
    __dni:str
    __telefono:str
    __saldo:float
    __cvu:str
    __porcentaje:float
    
    def __init__(self,Nya,Dni,Telefono,Saldo,Cvu,Porcentaje):
        self.__nya=Nya
        self.__dni=Dni
        self.__telefono=Telefono
        self.__saldo=Saldo
        self.__cvu=Cvu
        self.__porcentaje=Porcentaje
    
    def getNya(self):
        return self.__nya
    
    def getDni(self):
        return self.__dni
    
    def getTelefono(self):
        return self.__telefono
    
    def getSaldo(self):
        return float(self.__saldo)
    
    def getCvu(self):
        return self.__cvu
    
    def getPorcentaje(self):
        return self.__porcentaje
    
    def setSaldo(self,nuevosaldo):
        self.__saldo=float(nuevosaldo)
    
    def SetSaldo(self,new):
        self.__saldo=new
    
    def setSalditoCuenta(self,nuevoSaldo):
        self.__saldo=nuevoSaldo
    
    def setPorcentaje(self,nuevoPorcentaje):
        self.__porcentaje=nuevoPorcentaje
    
    def SetCuentas(self,newNya,newDni,newTelefono,newSaldo,newCvu,newPorcentaje):
        self.__nya=newNya
        self.__dni=newDni
        self.__telefono=newTelefono
        self.__saldo=newSaldo
        self.__cvu=newCvu
        self.__porcentaje=newPorcentaje
        
    
    def __str__(self):
        return f"Nya: {self.__nya} "f" Dni: {self.__dni} "f" Telefono: {self.__telefono} "f" Saldo: {self.__saldo} "f" Cvu: {self.__cvu} "f" Porcentaje: {self.__porcentaje}"