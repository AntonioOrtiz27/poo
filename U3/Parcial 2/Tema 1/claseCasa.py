from claseInmuebles import *
class Casa(Inmueble):
    __metros: int

    
    def __init__(self,Localidad, Direccion, Superficie,Metros):
        super().__init__(Localidad, Direccion, Superficie)
        self.__metros = Metros
   
        
    def __str__(self):
        return  super().__str__()+f"metros:{self.__metros}\n INMUEBLE TIPO CASA\n---------------------------------------------------------------------\n"
    
    def getMetros(self):
        return self.__metros
