
class Edificio:
    __id:int
    __nombre:str
    __direccion:str
    __nombre_empresa_c:str
    __cantidadP:int
    __cantD:int
    __departamento:list
    
    #Variables de Instancia
    def __init__(self,iD,Nombre,Direccion,CantidadP,empresa,CantD):
        self.__id=iD
        self.__nombre=Nombre
        self.__direccion=Direccion
        self.__nombre_empresa_c=empresa
        self.__cantidadP=CantidadP
        self.__cantD=CantD
        self.__departamento=[]
        
    def agregar_Dep(self,depa):
        self.__departamento.append(depa)
    @property
    def idd(self):
        return self.__id
    @property
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getNombreEmpresa(self):
        return self.__nombre_empresa_c
    def getCantidadP(self):
        return self.__cantidadP
    def getCantD(self):
        return self.__cantD
    @property
    def Departamento(self):
        return self.__departamento
    def __str__(self):
        return f"{self.__id} {self.__nombre} {self.__direccion} {self.__nombre_empresa_c} {self.__cantidadP} {self.__cantD}\n"