from clase2 import *
import csv

class gestor_lista:
    __lista: list
    
    def __init__(self):
        self.__lista=[]
        
    def cargarcsv(self):
        with open("ClientesFarmaCiudad.csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            next(reader)
            for fila in reader:
                unCliente = Cliente(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
                self.__lista.append(unCliente)
        
    def mostrar_lista(self):
        for objeto in self.__lista:
            print(objeto)
    
    def dni(self,GM):
        dni=str(input("Ingrese un dni:"))
        i:int=0
        band:bool=False

        while i<len(self.__lista) and band==False:
            objetito=self.__lista[i]
            if objetito.getDni()==dni:
                print(f"Cliente:{objetito.getNombre()} {objetito.getApellido()}   Numero de cuenta:{objetito.getNumcuenta()}\nSaldo Anterior:{objetito.getSaldo()}\nMovimientos")
                numC=objetito.getNumcuenta()
                saldoA=objetito.getSaldo()
                Saldito=GM.ActualizaSaldo(numC,saldoA)
                objetito.SetSaldo(Saldito)
                print(f"El saldo actualizado es: {objetito.getSaldo()}")
                band=True
            else:
                i+=1
        
        if band==False:
            print("No se encontro el cliente")
    
    def Tarjeta(self,GM):
        xDNI=str(input("Ingrese una DNI:"))
        i:int=0
        band:bool=False

        while i<len(self.__lista) and band==False:
            objetito=self.__lista[i]
            if objetito.getDni()==xDNI:
                nom=objetito.getNombre()
                ape=objetito.getApellido()
                numC=objetito.getNumcuenta()
                GM.verificar(nom,ape,xDNI,numC)
                band=True
            else:
                i+=1
                
        if not band:
            print("No existe el DNI ingresado")
  