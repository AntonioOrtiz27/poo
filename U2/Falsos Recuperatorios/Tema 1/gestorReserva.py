from claseReserva import *
import csv

class gestor_reserva:
    __lista: list
  
    def __init__(self):
        self.__lista=[]
    
    def cargarcsvlista(self):
        with open("Reservas.csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            for fila in reader:
                unaReservar = Reserva(*fila)
                self.__lista.append(unaReservar)
            print("Reservas Cargadas")
      
    def mostrar_lista(self):
        for objeto in self.__lista:
            print(objeto)

    def tieneReserva(self, num_cabaña):
        for reserva in self.__lista:
            if reserva.getNumc() == num_cabaña:
                return True
        return False
            
            
    def listar(self,GC):
        
        fecha=str(input("ingrese una fecha:"))
        print(f"\nReservas para la fecha: {fecha}")
        for objetito in self.__lista:
            if objetito.getFechai()==fecha:
                print("N°Cabaña Importe diario    Cantidad días    Seña    Importe a cobrar")
                imp=GC.obtenerImporte(objetito.getNumc())
                diario=imp/int(objetito.getCantd())
                Impcobrar=int(objetito.getCantd())*diario-float(objetito.getImporte())
                print(f"{objetito.getNum()}  {diario:>15} {objetito.getCantd():>10} {objetito.getImporte():>15}  {Impcobrar}\n")