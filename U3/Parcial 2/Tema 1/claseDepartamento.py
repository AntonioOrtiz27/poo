from claseInmuebles import *
class Departamento(Inmueble):
    __cantidad: int
    __numero: int 
    __numdepa: int
    __piso: int 
    
    def __init__(self, Localidad, Direccion, Superficie,Cantidad:int,NumeroM,Numdepa,Piso):
        super().__init__(Localidad, Direccion, Superficie)
        self.__cantidad = int(Cantidad)
        self.__numero = NumeroM
        self.__numdepa = Numdepa
        self.__piso = Piso
        
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
        return self.__cantidad * 17000 * 15
