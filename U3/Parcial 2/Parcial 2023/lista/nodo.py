from claseServicio import *
class Nodo:
    __servicio: Servicio
    __siguiente: object

    def __init__(self, otroservi: Servicio):
        self.__servicio = otroservi
        self.__siguiente = None
    
    def set_siguiente(self, agente):
        self.__siguiente = agente
    
    def getServicio(self):
        return self.__servicio
    
    def get_siguiente(self):
        return self.__siguiente