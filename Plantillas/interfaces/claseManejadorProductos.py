from zope.interface import Interface
from zope.interface import implementer
from interfaces import ICajero, ISupervisor


@implementer(ICajero)
@implementer(ISupervisor)
class ManejadorProductos:
    __productos=[]
    def __init__(self):
         self.__productos=[]     
    def agregarProducto(self, producto):
        self.__productos.append(producto)
        
        
    '''Método de la interface ICajero'''
    def buscarProductoPorDescripcion(self, descripcion):
        i=0
        bandera=False
        retorno=None
        while not bandera and i<len(self.__productos):
            unProducto=self.__productos[i]
            if unProducto.getDescripcion()==descripcion:
                bandera=True
            else:
                i+=1
        if bandera:
            retorno = self.__productos[i]
        return retorno
    
    
    '''Métodos de la interface ISupervisor'''
    def buscarProductoPorCodigo(self, codigo):
        i=0
        bandera=False
        retorno=None
        while not bandera and i<len(self.__productos):
            unProducto=self.__productos[i]
            if unProducto.getCodigo()==codigo:
                bandera=True
            else:
                i+=1
        if bandera:
            retorno = self.__productos[i]
        return retorno
    
    def modificarPrecio(self, codigo, precio):
        producto = self.buscarProductoPorCodigo(codigo)
        if producto == None:
            print('Producto código {}, no encontrado'.format(codigo))
        else:
            producto.modificarPrecio(precio)
