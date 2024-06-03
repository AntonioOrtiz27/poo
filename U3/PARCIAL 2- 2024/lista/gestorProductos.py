from claseCongelados import Congelado
from claseRefrigerados import Refrigerado
from claseProductos import Producto
import csv

class gestor_Productos:
    __lista:list

    def __init__(self):
        self.__lista=[]
    
    def cargar_Csv(self):
        with open("c:/Users/User/Desktop/PARCIAL 2/lista/productos.csv") as a:
            reader = csv.reader(a,delimiter=";")
            next(reader)
            for row in reader:
                if row[0] == "C":
                    uncongeladito=Congelado(row[1],row[2],row[3],row[4],row[5],row[6],float(row[7]),row[8],row[9],row[10],row[11],row[12])
                    self.__lista.append(uncongeladito)
                elif row[0] == "R":
                    unrefrigeradito=Refrigerado(row[1],row[2],row[3],row[4],row[5],row[6],float(row[7]),row[8])
                    self.__lista.append(unrefrigeradito)
                else:
                    print("no existe xd.")
        a.close()
        
    def mostrararchi(self):
        for objetito in self.__lista:
            print(objetito)
            
    def agregar_producto(self, producto):
            self.__lista.append(producto)
            print(f"Producto agregado: {producto}")
                
    def mostrar_agregados(self):
        for producto in self.__lista:
            print(producto)           
            
    def almacenado(self,pos):
        nashe=self.__lista[pos]
        if isinstance(nashe,Refrigerado):
                print(f"En la posicion {pos} se encuentra un producto de tipo Refrigerado.")
        elif isinstance(nashe,Congelado):
                print(f"En la posicion {pos} se encuentra un producto de tipo Congelado.")

    def cantidad(self):
        cont1:int=0
        cont2:int=0
        for lista in self.__lista:
            if isinstance(lista,Refrigerado):
                cont1+=1
            elif isinstance(lista,Congelado):
                cont2+=1
        print(f"Cantidad de productos del tipo Congelado: {cont2}.")
        print(f"Cantidad de productos del tipo Refrigerado: {cont1}.")

    def recorrer(self):
        print("Todos los productos.")
        importe_refrigerados:float = 0
        importe_congelados:float = 0
        
        for lista in self.__lista:
            importesito = lista.importe()
            print(f"Nombre: {lista.getNombre()}\nPais: {lista.getPais()}\nTemperatura: {lista.getTemperatura()}")
            if isinstance(lista, Refrigerado):
                importe_refrigerados += importesito
            elif isinstance(lista, Congelado):
                importe_congelados += importesito

        print(f"Importe de venta de los productos refrigerados: {importe_refrigerados}")
        print(f"Importe de venta de los productos Congelados: {importe_congelados}")