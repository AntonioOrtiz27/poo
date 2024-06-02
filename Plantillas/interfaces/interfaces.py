
from zope.interface import Interface
   
class ICajero(Interface):
    def buscarProductoPorDescripcion(descripcion):
        pass
   
class ISupervisor(Interface):
    def buscarProductoPorCodigo(codigo):
        pass
    def modificarPrecioProducto(codigo, precio):
        pass
