from ClaseMovimientos import * 
import csv
import numpy as np
#ARREGLO NUMPY CARGA


class GestorMovimientos:
    __arreglo:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int

    def __init__(self):
        self.__dimension=0
        self.__cantidad=0
        self.__incremento=1
        self.__arreglo= np.empty(0,dtype=Movimiento)
    
    def agregarMovimiento(self,unmov:Movimiento):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo=np.resize(self.__arreglo,(self.__dimension))
        self.__arreglo[self.__cantidad]=unmov
        self.__cantidad+=1
    
    def mostrar_arreglo(self):
        for movimiento in self.__arreglo:
            print(movimiento)   
            
    def csvMovimientos(self):
        with open('MovimientosAbril2024.csv', newline='') as a:
            reader = csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                unmov=Movimiento(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
            self.agregarMovimiento(unmov)
            
    def MostrarDatos(self,tarjeta,saldoAnterior):
        acum=0
        acum2=0
        movimientos=[]
        for arreglito in self.__arreglo:
            if arreglito.get_NumTarjeta()==tarjeta:
                if arreglito.get_tipoMov()=="C":
                    acum+=arreglito.get_Importe()
                elif arreglito.get_tipoMov()=="P":
                    acum2 += arreglito.get_Importe()
                movimientos.append(arreglito)
            
            SaldoActualizado=saldoAnterior+acum-acum2
            
        print(f"""Fecha        Descripción          Importe         Tipo de movimiento""")
        for movimiento in movimientos:        
            print(f"""{movimiento.get_Fecha()}     {movimiento.get_Descripcion()}        {movimiento.get_Importe()}         {movimiento.get_tipoMov()}""")      
            
        print(f"El saldo actualizado es: {SaldoActualizado}")


    def Mostrardatos2(self,tarjeta,nom,ape):
        for datos in self.__arreglo:
            if datos.get_NumTarjeta()==tarjeta:
                if  datos.get_tipoMov()=="C" or datos.get_tipoMov()=="P":
                    print(f"El cliente {nom} {ape} si tuvo movimientos en el Mes de Abril")
                else:
                    print("Nombre y Apellido del cliente que NO tuvo movimientos en abril de 2024")
                    print(f"Nombre: {nom} Apellido: {ape}")
        
    def OrdenarMovimientos(self):
        self.__arreglo.sort()
        
