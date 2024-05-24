from Matricula import *
import csv

class gestor_lista_3:
    __lista: list
  
    def __init__(self):
        self.__lista=[]
    
    def cargarcsvlista_3(self,GE,GP):
        with open("matricula.csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            next(reader)
            for fila in reader:
                unamatri = Matricula(fila[0],GE.buscarempleado(fila[1]),GP.buscarprograma(fila[2]))
                self.__lista.append(unamatri)
      
    def mostrar_lista_3(self):
        for objeto in self.__lista:
            print(objeto)
            
