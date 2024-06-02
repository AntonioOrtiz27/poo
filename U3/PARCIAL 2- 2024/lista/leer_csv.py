import csv

def leer_csv(self):
    with open('Vehiculos.csv','r', newline='',encoding='UTF-8') as archivo:
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            objeto = clase(*fila)
            self.agregar(objeto)
    archivo.close()
    
    with open('Vehiculos.csv','r',newline='',encoding='UTF-8') as archivo:
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            if len(fila)==7:
                objeto = V_pasajeros(*fila)
                self.agregar_en_orden(objeto)
            else:
                objeto = V_carga(*fila)
                self.agregar_en_orden(objeto)
    archivo.close()

