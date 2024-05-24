from claseMoto import *
import csv
import os
class gestor_motos:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
        
    def cargar_Csv_Motos(self):
        os.system("cls")
        with open("datosMotos.csv") as archi:
            reader=csv.reader(archi,delimiter=";")
            next(reader)
            for fila in reader:
                unpedido=Moto(fila[0],fila[1],fila[2],fila[3])
                self.__lista.append(unpedido)
        print("Motos cargadas correctamente")
        archi.close()
        
    def mostrar_motos(self):
        for moto in self.__lista:
            print(moto)
            
    def validarMoto(self,patente,pedido):
        i:int=0
        band:bool=False
        while i<len(self.__lista) and band==False:
            objeto=self.__lista[i]
            if self.__lista[i].get_patente()==patente:
                print(f"La moto existe,y corresponde al pedido numero {pedido} a cargo de {objeto.get_nya()}")
                band=True
            else:
                i+=1
        
        if band!=True:
            print("La moto no existe")
            
    def mostrarincisoTres(self,promedio,patente):
        i:int=0
        band:bool=False
        while i<len(self.__lista) and band==False:
            objeto=self.__lista[i]
            if objeto.get_patente()==patente:
                print(f"El tiempo real promedio de los pedidos de la moto {patente} a cargo de {objeto.get_nya()} es: {promedio}")
                band=True
            else:
                i+=1
        
        if band!=True:
            print("No se encontro el nombre de la persona a cargo de la moto.")
    

    def verificarpatente(self,GP):
        for moto in self.__lista:
            Patentes=moto.get_patente()
            Nya=moto.get_nya()
            GP.mostrarincisoTePuse(Patentes,Nya)
        
  
     
            

