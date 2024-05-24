from ClaseClientes import *
import csv

class GestorClientes:
    __lista:list
    
    def __init__(self):
        self.__lista=[]

    def csvCliente(self):
        with open('ClientesAbril2024.csv', newline='') as a:
            reader = csv.reader(a,delimiter=";")
            for fila in reader:
                uncliente=clientes(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
                self.__lista.append(uncliente)
                
    def BuscarDNI(self,GM):
        Dni=input("Ingrese dni:")
        i=0
        band=False
        while i<len(self.__lista) and band==False:
            estado=self.__lista[i]    
            if estado.get_DNI()==Dni:
                band=True
                tarjeta=estado.get_NumTarjeta()
            else:
                i+=1
                
        if band==True:
            print("EL DNI existe")
            print(f"""Cliente:{estado.get_Nombre()} {estado.get_Apellido()}   Numero de Tarjeta:{estado.get_NumTarjeta()}
Saldo Anterior:{estado.get_Saldo()}
--------------------------------------------------------------------
Movimientos""")
        else:
            print("EL DNI no existe")
            
        saldoAnterior= estado.get_Saldo()
        
        saldoact=GM.MostrarDatos(tarjeta,saldoAnterior)
        self.__lista[i].setSaldo(saldoact)
        
    def nomyape(self,GM):
        i=0
        Tarjet=input("Ingrese numero de tarjeta:")
        bandera=False
        while i<len(self.__lista) and bandera is False:
            estadoCliente=self.__lista[i]
            if estadoCliente.get_NumTarjeta()==Tarjet:
                bandera=True
                nom=estadoCliente.get_Nombre()
                ape=estadoCliente.get_Apellido()
            else:
                i+=1
        
        GM.Mostrardatos2(Tarjet,nom,ape)