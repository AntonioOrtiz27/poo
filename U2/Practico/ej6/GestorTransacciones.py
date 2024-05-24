from ClaseTransaccion import *
import csv

class gestor_Transacciones:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
    
    def mostrar_lista(self,transacciones):
        for transacciones in self.__lista:
            print(transacciones)
            
    def csv_transacciones(self):
        with open("transaccionesBilletera.csv") as a:
            reader=csv.reader(a,delimiter=",")
            next(reader) #salta la primera fila del csv, que es el titulo de las columnas
            for fila in reader:
                unaTrans=transaccion(fila[0],fila[1],float(fila[2]),(fila[3]))
                self.agregar_transaccion(unaTrans)
        a.close()
        
    def agregar_transaccion(self,unaTrans):
        self.__lista.append(unaTrans)
        
    def actualizaSaldo(self,cvu,s):
        tran:int=0
        for tran in self.__lista:
            if tran.get_cvu()==cvu and tran.get_tipo()=='C':
                s += tran.get_importe()
            elif tran.get_cvu()==cvu and tran.get_tipo()=='D':
                s -= tran.get_importe()
    
        return s
    
    def actualizaSaldoCuenta(self,Cvu,saldito):
        for tran in self.__lista:
            if tran.get_cvu()==Cvu and tran.get_tipo()=='C':
                saldito += tran.get_importe()
                print(f"Numero de Transaccion:{tran.get_numT()} "f" Tipo:{tran.get_tipo()} "f" importe:{tran.get_importe()} ")
            elif tran.get_cvu()==Cvu and tran.get_tipo()=='D':
                saldito -= tran.get_importe()
                print(f"Numero de Transaccion:{tran.get_numT()} "f" Tipo:{tran.get_tipo()} "f" importe:{tran.get_importe()} ")

    
        return saldito
                    