from zope.interface import Interface
   
class ICajero(Interface):
    def mostrar():
        pass
    def buscar(dato):
        pass
   
class ISupervisor(Interface):
    def agregar(dato):
        pass
    def insertar(indice, dato):
        pass
