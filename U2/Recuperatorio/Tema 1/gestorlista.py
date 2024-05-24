from claseNacimientos import *
import csv

class gestor_lista:
    __lista: list
  
    def __init__(self):
        self.__lista=[]
    
    def cargarcsvlista(self):
        with open(r"c:\Users\User\Documents\GitHub\poo\U2\Recuperatorio\Tema 1\Nacimientos.csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            next(reader)
            for fila in reader:
                unNacimiento = Nacimiento(*fila)
                self.__lista.append(unNacimiento)
      
    def mostrar_lista(self):
        for objeto in self.__lista:
            print(objeto)
            
    def obtenerParto(self,dni):
        i:int=0
        band:bool=False
        for objetito in self.__lista:   
            if dni==objetito.getDni():
                return objetito.getTipo()
            
    def pesoaltura(self,dni):
        print("Peso         Altura")
        for objetito in self.__lista:
            if dni==objetito.getDni():
                print(f"{objetito.getPeso()}        {objetito.getAltura()}")
                

    def obtenerDni(self,dni):
        for objetito in self.__lista:
            if dni==objetito.getDni():
                return objetito.getDni()
            
    def obtenerFecha(self,dni):
        for ob in self.__lista:
            if dni==ob.getDni():
                return ob.getFecha()
    
    def mostrar_Mas_de_unNac(self,GM):
    
        for i in range(len(self.__lista)):
            for j in range(i+1, len(self.__lista)): 
                    if self.__lista[i] == self.__lista[j]:
                        print("Datos de mamas con mas de un parto:")
                        GM.mostrarMamaxParto(self.__lista[i].getDni())
                
    
