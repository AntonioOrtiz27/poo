from Clasecancha import *
import csv
import numpy as np

class gestor_cancha:
    __arreglo:np.ndarray
    __cantidad:int
    __incremento:int
    __dimension:int

    def __init__(self):
        self.__arreglo=np.empty([0],dtype=cancha)
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=1
    
    def agregar(self,unaCancha:cancha):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=unaCancha
        self.__cantidad+=1

    def cargarCancha(self):
        with open("Canchas.csv")as a:
            reader=csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                unaCancha=cancha(*fila)
                self.agregar(unaCancha)
            print("Canchas Cargadas.")
        a.close()

    def mostrar1(self):
        for cancha in self.__arreglo:
            print(cancha)

    def minutitos(self,ide,GA):
        i:int=0
        band:bool=False
        while i<len(self.__arreglo) and band==False:
            objetito=self.__arreglo[i]
            if objetito.getid()==ide:
                iddd=objetito.getid()
                GA.mostrarCant(iddd)
                band=True
            else:
                i+=1
        
        if band is not True:
            print("No se encontro la cancha.")
    
    def obtener_importe_por_hora(self, id_cancha):
        c:float=0
        for cancha in self.__arreglo:
            if cancha.getid() == id_cancha:
                c=cancha.getImporte()/60
                return c

    def calcular_importe(self,idd):
        imp:float=0
        for ob in self.__arreglo:
            if idd == ob.getid():
                imp=ob.getImporte()
                return imp
