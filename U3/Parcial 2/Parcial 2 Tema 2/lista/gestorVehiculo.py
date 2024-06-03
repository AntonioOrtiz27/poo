from claseAutobus import Autobuses
from claseVanes import Vanes
from claseVehiculo import Vehiculo
import csv

class gestor_Vehiculo:
    __lista:list
    
    def __init__(self):
        self.__lista = []
    
    def cargarcsv(self):
        with open("c:/Users/User/Desktop/POO/U3/Parcial 2/Parcial 2 Tema 2/lista/vehiculos.csv") as a:
            reader=csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                if fila[0] == "V":
                    unVan = Vanes(fila[1],fila[2],int(fila[3]),int(fila[4]),float(fila[5]),float(fila[6]),float(fila[7]),fila[8]) #pacheco bautista
                    self.__lista.append(unVan)        
                elif fila[0] == "A":
                    unautobus = Autobuses(fila[1],fila[2],int(fila[3]),int(fila[4]),float(fila[5]),float(fila[6]),float(fila[7]),fila[8],fila[9])
                    self.__lista.append(unautobus)     
        print("cargados") 
        a.close()  
        
    def mostrarcsv(self):
        for objetito in self.__lista:
            print(objetito)
            
    def agregar(self,objetinho):
        self.__lista.append(objetinho)
        print(f"Productinho agregadinho:\n{objetinho}")
        
    def mostrar_Agregado(self):
        for objtinhoJR in self.__lista:
            print(objtinhoJR)
            
    def buscar(self,pos):# se podria hacer un caso hipotetico con while?
        objetinhoJR=self.__lista[pos]
        if isinstance(objetinhoJR,Vanes):
            print(f"En la posicion {pos} se encuentra un vehiculo de tipo Vanes.")
        elif isinstance(objetinhoJR,Autobuses):
            print(f"En la posicion {pos} se encuentra un vehiculo de tipo Autobus.")
    
    def cantidad(self):
        contador:int=0
        contador2:int=0
        for v in self.__lista:
            if(isinstance(v,Vanes)):
                contador+=1
            elif(isinstance(v,Autobuses)):
                contador2+=1
        print(f"La cantidad de Autobuses es {contador2} y la cantidad de Vanes {contador}")

    def bytarifa(self):
        for pachequinhosalvaje in self.__lista:
            tarifabus=pachequinhosalvaje.tarifa()
            tarifaVanes=pachequinhosalvaje.tarifa()
            print(f"Modelo:{pachequinhosalvaje.getModelo()}\n Año Fabricacion:{pachequinhosalvaje.getAno()}\nCapacidad:{pachequinhosalvaje.getCapacidad()} ")
            print(f"Tarifa de Servicio de Autobuses:{tarifabus:.2f}")
            print(f"Tarifa de Servicio de Vanes:{tarifaVanes:.2f}")