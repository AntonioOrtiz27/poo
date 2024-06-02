import unittest
from lista import Lista

class Test(unittest.TestCase):
    __lista: list
    
    def setUp(self):
        self.__lista = Lista()
        for i in range(5):
            self.__lista.agregar(i)
            
    def test_buscar(self):
        self.assertEqual(self.__lista.buscar(2), 2)
        
    def test_buscar_dato(self):
        self.assertEqual(self.__lista.buscar_dato(3), 3)
        
    def test_agregar(self):
        self.__lista.agregar(7)
        self.assertEqual(self.__lista.buscar_dato(5), 7)
        
    def test_insertar(self):
        self.__lista.insertar(2, 8)
        self.assertEqual(self.__lista.buscar_dato(2), 8)
        
        
if __name__ == '__main__':
    unittest.main()