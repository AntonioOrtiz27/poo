from clase1 import *
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
        self.__arreglo= np.empty(0,dtype=Movimientos)
    
    def agregarMovimiento(self,unMov:Movimientos):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo=np.resize(self.__arreglo,(self.__dimension))
        self.__arreglo[self.__cantidad]=unMov
        self.__cantidad+=1
  
    def cargarcsv(self):
        with open('MovimientosAbril2024.csv', newline='') as a:
            reader = csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                unMov=Movimientos(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
                self.agregarMovimiento(unMov)
            
    def mostrar_arreglo(self):
        for movimiento in self.__arreglo:
            print(movimiento)   
            
    def ActualizaSaldo(self,numC,saldoA):
        for objetito in self.__arreglo:
            if objetito.getNumCuenta() == numC:            
                print(f"""
                Fecha         Descripcion    Importe    Tipo Mov  
                {objetito.getFecha()}    {objetito.getDescripcion()}    {objetito.getImporte()}    {objetito.getTipo()}  
                  """)
                if objetito.getTipo() == "C":
                    saldoA=saldoA+objetito.getImporte()
                if objetito.getTipo() == "D":
                    saldoA=saldoA-objetito.getImporte()
                    
        return saldoA

        
    def verificar(self, nom, ape, xDNI, numC):
        cont = 0
        
        for objetito in self.__arreglo:
            if numC == objetito.getNumCuenta():
                if objetito.getTipo() == "C" or objetito.getTipo() == "D":
                    cont += 1

        if cont>0:
            print(f"Cliente {nom} {ape} con dni {xDNI} tuvo {cont} movimiento/s en el mes de Abril de 2024.")
        else:
            print(f"No se encontraron movimientos en el mes de Abril de 2024 de {nom} {ape}.")
    
    def ordenar(self):
        self.__arreglo=sorted(self.__arreglo)
        print("Movimientos ordenados de menor a mayor por Numero de cuenta.")
        for objetito in self.__arreglo:
            print(objetito)
        print("Movimientos Ordenados")


            
