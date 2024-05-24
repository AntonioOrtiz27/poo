from empleado import *
import csv

class gestor_lista_1:
    __lista: list
  
    def __init__(self):
        self.__lista=[]
    
    def cargarcsvlista(self):
        with open("empleado.csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            next(reader)
            for fila in reader:
                unempleado = Empleado(*fila)
                self.__lista.append(unempleado)
                
                
    def buscarempleado(self,idd):
        i = 0
        band = False
        if idd == None:
            return None
        else:
            while i < len(self.__lista) and not band:
                if self.__lista[i].getId() == idd:
                    band = True
                else:
                    i+=1
            if band:
                return self.__lista[i]
      
    def mostrar_lista(self):
        for objeto in self.__lista:
            print(objeto)
            
    def obtenerId(self,idd):
        i: int = 0
        j:int=0
        band:bool=False
        while i < len(self.__lista) and band==False:
            objetito = self.__lista[i]
            if idd == int(objetito.getId()):
                band=True
            else:
                i+=1
        
        if band is not True:
            print("El empleado no existe")
        else:
            print("Programa             Duracion")
            while j < len(self.__lista[i].getMatricula()):
                if self.__lista[i].getMatricula()[j].getPrograma() != None and self.__lista[i].getMatricula()[j].getPrograma().getNom() != None: #contempla la posibilidad de que si haya usuario, pero que al programa que este matriculado no exista(no se haya ingresado) o que no exista el nombre
                    band = True #es indistinto
                    print(f"{self.__lista[i].getMatricula()[j].getPrograma().getNom()}   {self.__lista[i].getMatricula()[j].getPrograma().getDuracion()}hs \n")
                j+=1
