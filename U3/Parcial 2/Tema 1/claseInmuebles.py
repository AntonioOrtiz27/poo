class Inmueble:
    __localidad: str
    __direccion: str 
    __superficie: int

    
    def __init__(self,Localidad,Direccion,Superficie):
        self.__localidad = Localidad
        self.__direccion = Direccion
        self.__superficie = Superficie
        
    def __str__(self):
        return f"localidad:{self.__localidad}\ndireccion:{self.__direccion}\nsuperficie:{self.__superficie}\n"
    
    def getLocalidad(self):
        return self.__localidad
    
    def getDireccion(self):
        return self.__direccion
    
    def getSuperficie(self):
        return self.__superficie
    

