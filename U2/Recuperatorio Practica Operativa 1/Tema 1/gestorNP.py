from claseMamas import *
import numpy as np
import csv

#ARREGLO NUMPY CARGAR
class gestor_numpy:
    __arreglo:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int

    def __init__(self):
        self.__dimension=0
        self.__cantidad=0
        self.__incremento=1
        self.__arreglo= np.empty(0,dtype=Mamas)
    
    def agregarMovimiento(self,unamama:Mamas):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo=np.resize(self.__arreglo,(self.__dimension))
        self.__arreglo[self.__cantidad]=unamama
        self.__cantidad+=1
  
    def cargarcsv(self):
        with open(r"c:\Users\User\Documents\GitHub\poo\U2\Recuperatorio\Tema 1\Mamas.csv", newline='', encoding='utf-8') as a:    # Your code to process the CSV file
            reader = csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                unamama=Mamas(*fila)
                self.agregarMovimiento(unamama)
            
    def mostrar_arreglo(self):
        for movimiento in self.__arreglo:
            print(movimiento)   
            
    def mostrar_listado(self,dni,GN):
        i:int=0
        band:bool=False
        while i < len(self.__arreglo) and band==False:
            objetito=self.__arreglo[i]
            if objetito.getDni()==dni:
                p=GN.obtenerParto(objetito.getDni())
                print(f"Apellido y Nombre: ,{objetito.getNya()}\n Edad: {objetito.getEdad()}\n Parto:{p}\n")
                print(f"Bebe/s de {objetito.getNya()}:")
                GN.pesoaltura(objetito.getDni())
                band=True
            else:
                i+=1
        if band is not True:
            print("no se encontro el dni ingresado")


    def mostrarMamaxParto(self, dni):
            i=0
            band= False
            while i < self.__cantidad and band==False:
                if self.__arreglo[i].getDni() == dni:
                    band = True
                    Mama = self.__arreglo[i]
                else:
                    i += 1

            if band:
                print(f"Apellido y nombre: {Mama.getNya()}")
                print(f"DNI: {Mama.getDni()}")
                print(f"Edad: {Mama.getEdad()}")
