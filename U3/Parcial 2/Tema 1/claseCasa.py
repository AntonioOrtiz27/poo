from claseInmuebles import *
class Casa(Inmueble):
    __metros: float

    
    def __init__(self,Localidad, Direccion, Superficie,Metros):
        super().__init__(Localidad, Direccion, Superficie)
        self.__metros = float(Metros)
   
        
    def __str__(self):
        return  super().__str__()+f"metros:{self.__metros}\n INMUEBLE TIPO CASA\n---------------------------------------------------------------------\n"
    
    def getMetros(self):
        return self.__metros

    def calculito(self):
        return self.__metros * 1.80 * 20000 * 15
    
    
