import unittest
from claseServicioEmbalaje import ServicioE
from claseServicioTransporte import ServicioT
from claseServicio import Servicio
from lista import Lista

class Test(unittest.TestCase):
    
    def setUp(self):
        self.__lista = Lista() 
    
    def test_agregar(self):  
        servicio_transporte = ServicioT(Nome="transporte abc", 
                                        NomC="antonio",
                                        Direccion="9 de julio",
                                        Fecha="20/05/2005",
                                        Comision=131,
                                        Precio = 87,
                                        Peso=12,
                                        DireccionDestino="Buenos aires",
                                        Hora=1)
        servicio_embalaje = ServicioE(Nome="embalaje abc", 
                                        NomC="lauta",
                                        Direccion="santa lucia",
                                        Fecha="20/05/2005",
                                        Comision=131,
                                        Precio=12,
                                        Peso=12,
                                        Cantidad=2)
        print("EL metodo agregar objetos al final de la lista, definida por el programador funciona.")
        
        self.__lista.agregar_por_cabeza(servicio_embalaje)
        self.assertIn(servicio_embalaje, self.__lista, "El servicio de embalaje no se agregó correctamente a la lista")
        self.__lista.agregar_por_cabeza(servicio_transporte)
        self.assertIn(servicio_transporte, self.__lista, "El servicio de transporte no se agregó correctamente a la lista")

if __name__ == '__main__':
    unittest.main()