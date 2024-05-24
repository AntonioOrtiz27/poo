from clasePedido import *
import csv
import os
class gestor_pedidos:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
        
    def get_lista_pedidos(self):
        return self.__lista
        
    def cargar_Csv_Pedidos(self):
        os.system("cls")
        with open("datosPedidos.csv") as archi:
            reader=csv.reader(archi,delimiter=";")
            next(reader) 
            for fila in reader:
                unpedido=Pedido(fila[0],int(fila[1]),fila[2],int(fila[3]),int(fila[4]),float(fila[5]))
                self.__lista.append(unpedido)
        print("Pedidos cargados correctamente")
        archi.close()
        
    def mostrar_pedidos(self):
        for pedido in self.__lista:
            print(pedido)
            
    def verificar(self,GM,patente):
        i:int=0
        band:bool=False
        while i < self.__lista.__len__() and band==False:
            if self.__lista[i].getPatente()==patente:
                pedido=self.__lista[i].getId()
                band=True
            else:
                i+=1
        
        if band!=True:
            print("No existe la patente ingresada, por lo tanto")
        else:
            print("La patente existe")
            
        GM.validarMoto(patente,pedido)
        
    def actualizar(self,pat,idd,Tr):
        print("Actualizando tiempo real con los siguientes valores")
        print(f"Patente: {pat}")
        print(f"ID del pedido: {idd}")
        i:int=0
        bandera:bool=False
        while i < len(self.__lista) and bandera==False:
            ob=self.__lista[i]
            if ob.getPatente()==pat and ob.getId()==idd:
                ob.setTiempoReal(Tr)
                print(f"El tiempo real actualizado del pedido {idd} es: {ob.getTiempoR()}")
                print(f"Y su tiempo estimado era: {ob.getTiempoE()}")
                bandera=True
            else:
                i+=1
                
        if not bandera:
            print("El tiempo real no fue actualizado. No se encontró el pedido.")       
            
    def nyaConductor(self,GM):
        patente=input("Ingrese la patente de la moto: ")
        contador:int=0
        acum:int=0
       
        for objetito in self.__lista:
            if objetito.getPatente()==patente:
                contador+=1
                acum+=objetito.getTiempoR()
                promedio=acum/contador
                print("ID       Comida pedida       tiempo estimado         tiempo real")
                print(f"{objetito.getId()}       {objetito.getComidas():>10}            {objetito.getTiempoE():>10}       {objetito.getTiempoR():>10}")
                
        if contador==0:
            print("El tiempo real no fue actualizado. No se encontró el pedido.")
            
        GM.mostrarincisoTres(promedio,patente)
            
    def mostrarincisoTePuse(self,Patentes,Nya):
        sum:int=0
        for pedido in self.__lista:
            if pedido.getPatente()==Patentes:
                print(f"\nPatente de Moto:{Patentes}\nConductor:{Nya}")
                print("Id  TiempoE  TiempoR  Precio ")
                print(f"{pedido.getId()}     "f"{pedido.getTiempoE()}      "f"{pedido.getTiempoR()}     "f"{pedido.getPrecio()}")
                sum+=pedido.getPrecio()
                comi=sum*0.20
        print(f"Total: {sum}")
        print(f"Comisión:{comi}")
        
        
    def ordenar(self):
        os.system("cls")
        self.__lista = sorted(self.__lista)
        print("Lista de pedidos ordenados:")
        for pedido in self.__lista:
            print(pedido)
            
        print("Pedidos Ordenados")