class Movimientos:
    __numCuenta: str
    __fecha: str 
    __descripcion: str
    __tipo: str
    __importe: float
    
    def __init__(self,Numcuenta,Fecha,Descripcion,Tipo,Importe):
        self.__numCuenta = int(Numcuenta)
        self.__fecha = Fecha
        self.__descripcion = Descripcion
        self.__tipo = Tipo
        self.__importe = float(Importe)
        
    def __str__(self):
        return f"numCuenta:{self.__numCuenta} fecha:{self.__fecha} descripcion:{self.__descripcion} tipo:{self.__tipo} importe:{self.__importe}\n"
    
    def getNumCuenta(self):
        return self.__numCuenta
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe

    def __lt__(self,other):
        return self.__numCuenta < other.getNumCuenta()
       