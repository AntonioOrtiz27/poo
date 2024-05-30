from nodo import Nodo
from claseServicio import Servicio
from claseServicioEmbalaje import ServicioE
from claseServicioTransporte import ServicioT

class Lista:
    __cabeza: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__cabeza = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        self.__actual = self.__cabeza
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__indice = 0
            self.__actual = self.__cabeza
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getServicio()
            self.__actual = self.__actual.get_siguiente()
            return dato
        
    def mostrar(self):
        print("Elementos de la lista:")
        for dato in self:
            print(dato)
        
    def agregar(self, dato):
        aux = self.__cabeza
        nodo = Nodo(dato)
        if aux != None:
            while aux.get_siguiente() != None:
                aux = aux.get_siguiente()
            aux.set_siguiente(nodo)
        else: 
            self.__cabeza = nodo
        self.__tope += 1
    
    def agregar_por_cabeza(self, dato):
        nodo = Nodo(dato)
        nodo.set_siguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__tope += 1


    def buscar(self, dato):
        aux = self.__cabeza
        indice = 0
        while aux is not None:
            if aux.get_dato() == dato:
                return indice
            aux = aux.get_siguiente()
            indice += 1
        return -1
    
    def buscar_dato(self, indice):
        if 0 <= indice < self.__tope:
            aux = self.__cabeza
            for _ in range(indice):
                aux = aux.get_siguiente()
            return aux.get_dato()
        else:
            raise IndexError("Posicion incorrecta")


    def mostrarlistaTransporte(self):
        cont:int=0
        print("Servicios de transporte realizados:")
        print("Contratante          Costo Total")
        for lista in self:
            if isinstance(lista, ServicioT):
                costoTransporte= lista.Costito() + lista.getComision()
                print("{}                    {}".format(lista.getNomC(), costoTransporte))
                cont+= costoTransporte
        print("Total de costo: {}".format(cont))
        
    def mostrarlistaEmbalaje(self):
        cont:int=0
        for lista in self:
            if isinstance(lista, ServicioE):
                if lista.getPesito()>50:
                    cont+=1
                else:
                    print("no hay servicios de embalaje que superen los 50 kilos")
        print(f"Servicios de Embalaje realizados supera los 50 kg: {cont}")
        
    def mostrarfechas(self,fecha):
        cont:int=0
        contador:int=0
        for fechita in self:
            if fecha==fechita.getFecha():
                if  isinstance(fechita, ServicioT):
                    cont+=1
                elif isinstance(fechita, ServicioE):
                    contador+=1

        if cont==0 and contador==0:
            print("No hay servicios de transporte o de embalaje en la fecha seleccionada")
        else:
            if cont>contador:
                print(f"El servicio de tipo transporte para la fecha {fecha} es el que tuvo mas contrataciones")
            elif contador>cont:
                print(f"El servicio de tipo Embalajae para la fecha {fecha} es el que tuvo mas contrataciones")
            elif contador==cont:
                print(f"ambos servicios para la fecha {fecha} tienen las mismas contrataciones")