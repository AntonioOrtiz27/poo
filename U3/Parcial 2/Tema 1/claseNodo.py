from claseInmuebles import Inmueble
class Nodo:
    __inmueble: Inmueble 
    __siguiente: None
    def __init__(self, dato:Inmueble):
        self.__inmueble=dato
        
    @property
    def siguiente(self):
        return self.__siguiente   
     
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
  
    def getInmueble(self): 
        return self.__inmueble