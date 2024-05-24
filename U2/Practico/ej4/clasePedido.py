class Pedido:
    __patente:str
    __id:int
    __comidas:str
    __tiempoE:int
    __tiempoR:int
    __precio:float
    
    def __init__(self,Patente,idd:int,Comidas,TiempoE:int,TiempoR:int,Precio:float):
        self.__patente=Patente
        self.__id=idd
        self.__comidas=Comidas
        self.__tiempoE=TiempoE
        self.__tiempoR=TiempoR
        self.__precio=Precio
    
    def getPatente(self):
        return self.__patente
    
    def getId(self):
        return int(self.__id)
    
    def getComidas(self):
        return self.__comidas
    
    def getTiempoE(self):
        return int(self.__tiempoE)
    
    def getTiempoR(self):
        return int(self.__tiempoR)
    
    def getPrecio(self):
        return float(self.__precio)
    
    def setTiempoReal(self,otroTiempoR):
        self.__tiempoR=int(otroTiempoR)
    
    def __lt__(self, other):
        return self.__patente > other._Pedido__patente
    
    def __lt__(self, other):
        return self.__patente < other._Pedido__patente
    
    def __str__(self):
        return f"Patente: {self.__patente} "f"Id: {self.__id} "f" Comidas: {self.__comidas} "f" Tiempo de espera: {self.__tiempoE} "f" Tiempo Real: {self.__tiempoR} "f" Precio: {self.__precio}"