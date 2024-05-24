class Moto:
    __patente:str
    __marca:str
    __nya:str
    __km:float
    
    def __init__(self,Patente,Marca,Nya,Km:float):
        self.__patente=Patente
        self.__marca=Marca
        self.__nya=Nya
        self.__km=Km
    
    def get_patente(self):
        return self.__patente
    
    def get_marca(self):
        return self.__marca
    
    def get_nya(self):
        return self.__nya
    
    def get_km(self):
        return float(self.__km)
    
    def __str__(self):
        return f"Patente: {self.__patente} "f" Marca: {self.__marca} "f" Número de yas: {self.__nya} "f" Kilometraje: {self.__km}"
    
