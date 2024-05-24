from ClaseCuenta import *
import numpy as np
import csv

class gestor_cuenta:
    __arreglito:any
    
    def __init__(self):
        self.__arreglito=np.empty(0,dtype=cuenta)
            
    def csv_cuenta(self):
        with open("cuentaBilletera.csv") as a:
            reader=csv.reader(a,delimiter=",")
            next(reader) #salta la primera fila del csv, que es el titulo de las columnas
            lista=[]
            for fila in reader:
                unacuenta=(cuenta(fila[0],fila[1],fila[2],float(fila[3]),fila[4],float(fila[5])))
                lista.append(unacuenta)
            self.__arreglito=np.array(lista)
        a.close()
        
    def mostrarCuenta(self):
        print("Transacciones cargadas")
        for unaCuenta in self.__arreglito:
            print(unaCuenta)

    def informar(self,xdni,GT):
        i=0
        bandera=False
        while i < len(self.__arreglito) and bandera is False:
            objeto=self.__arreglito[i]
            if self.__arreglito[i].getDni()==xdni:
                print(f"Nombre y apellido: {objeto.getNya()} "f" Cvu: {objeto.getCvu()} ")
                print(f"Saldo Anterior: {objeto.getSaldo()}")
                cvu=objeto.getCvu()
                s=objeto.getSaldo()
                saldoact=GT.actualizaSaldo(cvu,s)
                self.__arreglito[i].setSaldo(saldoact)
                print(f"Saldo Actualizado: {objeto.getSaldo()}")
                bandera=True
            else:
                i+=1
                
        if bandera is False:
            print("No se encontro el DNI")
            
    def modificar(self,Pnuevo):
        for unaCuenta in self.__arreglito:
            unaCuenta.setPorcentaje(Pnuevo)
            print(f"Porcentaje nuevo para todas las cuentas es:")
            print(f"{unaCuenta}")
            
    def actualiza(self):
        for cuenta in self.__arreglito:
            porcentaje_diario = cuenta.getPorcentaje()/365
            if cuenta.getSaldo() > 0:
                x = cuenta.getSaldo() * (porcentaje_diario/100)
                y = cuenta.getSaldo() + x
                cuenta.SetSaldo(y)
                print(f"Saldo actualizado de la cuenta {cuenta.getDni()} es: {cuenta.getSaldo()}")
            else:
                print(f"No se puede actualizar la cuenta {cuenta.getDni()} porque su saldo es menor a 0")
    
    def saldoNuevo(self,GT):
        Cvu=str(input("ingrese cvu: "))
        i:int=0
        bandera=False
        while i < len(self.__arreglito) and bandera is False:
            objeto=self.__arreglito[i]
            if self.__arreglito[i].getCvu() == Cvu:
                print(f"Saldo anterior del cvu ingresado:{objeto.getSaldo()}")
                saldito=objeto.getSaldo()
                saldoact=GT.actualizaSaldoCuenta(Cvu,saldito)
                self.__arreglito[i].setSalditoCuenta(saldoact)
                print(f"Saldo Actualizado: {objeto.getSaldo()}")
                bandera=True
            else:
                i+=1
                
        if bandera is False:
            print("No se encontro el DNI")
            
            
    def cargar_Csv_Actualizado(self):
        nuevo_Csv="C:\Users\usuario\Desktop\POO\U2 POO\Ejercicios POO\Practica 2\ej6\archivosActualizados.csv"
        with open("archivosActualizados.csv")as archi:
            writer=csv.writer(archi,delimiter=";")
            next(writer)
            lista=[]
            for row in writer:
                cuentaActualizada=cuenta(row[0],row[1],row[2],row[3],row[5])
                lista.append(cuentaActualizada)
            self.__arreglito=np.array(lista)
        archi.close()
                
    
    
    
    
    
    
    
    

        

        