from ClaseAlquiler import *
import csv

class gestor_alquiler:
    __lista:list

    def __init__(self):
        self.__lista=[]

    def cargarAlquiler(self):
        with open("Alquiler.csv")as a:
            reader=csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                unAlquiler=Alquiler(*fila)
                self.__lista.append(unAlquiler)
            print("Alquileres Cargados.")
        a.close()

    def mostrar2(self):
        for alquiler in self.__lista:
            print(alquiler)

    def mostrarCant(self,iddd):
        sum:int=0
        for objetito in self.__lista:
            if objetito.getID()==iddd:
                sum+=int(objetito.getDuracion())
            
        print(f"Esta cancha estuvo alquilada {sum} minutos.")
  
          
    def listado(self, GC):
        self.__lista.sort()
        total_recaudado:int = 0
        d:float=0
        print("Hora  Id  Duración   Importe por hora  Importe alquiler")
        for alquiler in self.__lista:
            importe_por_hora = GC.obtener_importe_por_hora(alquiler.getID())
            importe_alquiler = GC.calcular_importe(alquiler.getID())
            total_recaudado += importe_alquiler
            d=alquiler.getDuracion() / 60
            print(f"{alquiler.getHora()}:{alquiler.getMinutos()}  {alquiler.getID()}  {d:>5}  {importe_por_hora:>15.2f}  {importe_alquiler:>15}")
        print(f"Total recaudado    {total_recaudado}")
        