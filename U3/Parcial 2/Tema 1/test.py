import unittest
from claseCasa import Casa
from claseDepartamento import Departamento

class TestImporteVenta(unittest.TestCase):
    def setUp(self):
        self.__casa=Casa("Rivadavia", "Guemes", 10, 10)
        self.__depto=Departamento("Capital", "Mitre", 10, 2, 10, 5, 3)

    def test_ImporteCasa(self):
        esperado = self.__casa.getMetros()*1.8*20000*15
        precioV=self.__casa.calculito()
        self.assertEqual(esperado,precioV)
    
    def test_ImporteDpto(self):
        esperado = self.__depto.getCantidad()*17000*15
        total=self.__depto.calculo()
        self.assertEqual(esperado,total)

if __name__ == '__main__':
    unittest.main()