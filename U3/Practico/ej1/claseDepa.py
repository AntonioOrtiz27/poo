class Departamento:
    __idd:str
    __nya:str
    __Numpiso:int
    __numDepa:int
    __cantDor:int
    __cantBanos:int
    __superficie:float
    
    def __init__(self,iDd, Nya, numpiso, NumDepa, CantDor, CantBanos, Superficie):
        self.__idd = iDd
        self.__nya = Nya
        self.__Numpiso = numpiso
        self.__numDepa = NumDepa
        self.__cantDor = CantDor
        self.__cantBanos = CantBanos
        self.__superficie = float(Superficie.replace(",","."))
    @property
    def getIdd(self):
        return self.__idd
    def getnya(self):
        return self.__nya
    @property
    def getNumpiso(self):
        return int(self.__Numpiso)
    def getNumdepa(self):
        return int(self.__numDepa)
    @property
    def getCantdor(self):
        return int(self.__cantDor)
    @property
    def getCantB(self):
        return int(self.__cantBanos)
    @property
    def Superficie(self):
        return float(self.__superficie)
    
    def __str__(self):
        return f"{self.__idd} {self.__nya} {self.__Numpiso} {self.__numDepa} {self.__cantDor} {self.__cantBanos} {self.__superficie}"
