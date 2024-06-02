from claseCabaña import *
import numpy as np
import csv

#ARREGLO NUMPY CARGAR
class gestor_cabaña:
    __arreglo:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int

    def __init__(self):
        self.__dimension=0
        self.__cantidad=0
        self.__incremento=1
        self.__arreglo= np.empty(0,dtype=Cabaña)
    
    def agregarMovimiento(self,unaCabaña:Cabaña):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo=np.resize(self.__arreglo,(self.__dimension))
        self.__arreglo[self.__cantidad]=unaCabaña
        self.__cantidad+=1
  
    def cargarcsv(self):
        with open('Cabañas.csv', newline='') as a:
            reader = csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                unaCabaña=Cabaña(*fila)
                self.agregarMovimiento(unaCabaña)
            print("Cabañas Cargadas")
            
    def mostrar_arreglo(self):
        for movimiento in self.__arreglo:
            print(movimiento)   
            
    def mostrarNumC(self, GR):
        canti=int(input("ingrese numero de huesped:"))
        for cabaña in self.__arreglo:
            if cabaña.capacidad() >= canti and not GR.tieneReserva(cabaña.getNum()):
                print(f"Cabaña {cabaña.getNum()} con capacidad para {cabaña.capacidad()} huéspedes")
                
    def obtenerImporte(self,num):
        for ob in self.__arreglo:
            if ob.getNum() == num:
                return int(ob.getImporte())

            