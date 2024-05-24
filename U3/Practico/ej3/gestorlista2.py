from Programa import *
import csv

class gestor_lista_2:
    __lista: list
  
    def __init__(self):
        self.__lista=[]
    
    def cargarcsvlista_2(self):
        with open("Programa.csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            for fila in reader:
                unprograma = Programa(*fila)
                self.__lista.append(unprograma)
                
    def buscarprograma(self,cod):
        i = 0
        band = False
        if cod == None:
            return None
        else:
            while i < len(self.__lista) and not band:
                if self.__lista[i].getCodigo() == cod:
                    band = True
                else:
                    i+=1
            if band:
                return self.__lista[i]
      
    def mostrar_lista_2(self):
        for objeto in self.__lista:
            print(objeto)
            
