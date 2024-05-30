import unittest
from claseServicio import Servicio
from lista import Lista
#Permite testear  el metodo agregar objetos a la lista item a)
class TestServicio(unittest.TestCase):
    def setUp(self):
        self.__lista = Lista()
        
    def test_agregar(self):# Creamos un objeto de tipo Servicio para agregar a la lista
        servicio = Servicio("FNCS", "Mondre", "Meglioli", "12m", 100.0)
        
        # Agregamos el servicio a la lista
        self.__lista.agregar(servicio)
        
        # Verificamos si el servicio se encuentra en la lista
        self.assertIn(servicio, self.__lista, "El servicio no se agregó correctamente a la lista")

if __name__ == '__main__':
    unittest.main()