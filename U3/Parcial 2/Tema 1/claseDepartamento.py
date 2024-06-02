from claseInmuebles import *
class Departamento(Inmueble):
    __cantidad: int
    __numero: int 
    __numdepa: int
    __piso: int 
    
    def __init__(self, Localidad, Direccion, Superficie,Cantidad:int,NumeroM,Numdepa,Piso):
        super().__init__(Localidad, Direccion, Superficie)
        self.__cantidad = int(Cantidad)
        self.__numero = int(NumeroM)
        self.__numdepa = int(Numdepa)
        self.__piso = int(Piso)
        
    def __str__(self):
        return super().__str__()+f"\ncantidad:{self.__cantidad}\nnumero:{self.__numero}\nnumdepa:{self.__numdepa}\npiso:{self.__piso}\n INMUEBLE TIPO DEPARTAMENTO\n---------------------------------------------------------------------\n"
    
    def getCantidad(self):
        return self.__cantidad
    
    def getNumeromono(self):
        return self.__numero
    
    def getNumdepa(self):
        return self.__numdepa
    
    def getpiso(self):
        return self.__piso
    
    def calculo(self):
        precio=float
        imp=float
        
        precio=self.__cantidad*17000
        imp=super().getSuperficie()* 15 *precio
        return imp
