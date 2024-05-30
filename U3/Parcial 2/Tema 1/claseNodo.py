from claseInmuebles import Inmueble
class Nodo:
    __inmueble: Inmueble 
    __siguiente: object
    def __init__(self, Inmueble):
        self.__inmueble=Inmueble
        self.__siguiente=None
        
    @property
    def siguiente(self):
        return self.__siguiente   
     
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
  
    def getInmueble(self): 
        return self.__inmueble