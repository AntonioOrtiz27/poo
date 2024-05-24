import numpy as np

class menu:
    __arreglo:np.ndarray

    def __init__(self):
        self.__arreglo = np.empty([2,2],dtype=float)

    def test(self):
        print("---CARGA DE VENTAS PARA LAS SUCURSALES---")
        for i in range(2):
            print(f"Facturacion de la empresa {i+1}")
            for j in range(2):
                self.__arreglo[i][j]=float(input(f"ingrese facturacion del dia {j+1}:"))


    def acum(self,day,number,factura):
        self.__arreglo[day-1][number-1]+=factura
        print(f"el nuevo importe es: {self.__arreglo[day-1][number-1]}")

    def total(self,num):
        sum=np.sum(self.__arreglo[num-1])
        print(f"el total de facturacion para la sucursal {num} es de: {sum}")
        
    def factura(self,dia,i=0):
        max=-1
        for i in range(2):
            self.__arreglo[i][dia-1]<max
            max=self.__arreglo[i][dia-1]
            aux=i+1
        
        print(f"la sucursal que mas facturo el dia {dia} es la sucursal {aux} con un importe de {max}$")
        
    def minimo(self):
        min=99999
        for i in range(2):      
            for j in range(2):
                if self.__arreglo[i][j]<min:
                    min=self.__arreglo[i][j]
                    auxiliar=i+1
        
        print(f"La sucursal que menos facturo en la semana es la Sucursal {auxiliar}.")
        
    def Total_Facturado(self):
        for i in range(2):
            for j in range(2):
                sum=np.sum(self.__arreglo)
                
        print(f"Total facturado por todas las sucursales en toda la semana: {sum}$.")
            
def menuOptions():
    op=int(input("""
        ----MENU DE OPCIONES----")
        [1].Ingrese dia de la semana,numero de sucursal e importe de factura, para acumular la facturacion
        [2].Seleccione sucursal,(para calcular el total de facturacion para la sucursal)
        [3].Seleccione dia de la semana (para obtener la sucursal que mas facturo ese dia)
        [4].Facturacion de la sucursal que menos facturo en la semana 
        [5].FActuracion Total de todas las sucursales en toda la semana
        
        [0]Para Salir
        --->"""))
    return op



if __name__=="__main__":
    arreglo=menu()
    arreglo.test()
    opcion=menuOptions()
    while opcion!=0:
        if opcion==1:
            day=int(input("ingrese dia de la senana"))
            number=int(input("ingrese numero de la sucursal"))
            factura=float(input("ingrese importe de una factura"))
            arreglo.acum(day,number,factura)
        elif opcion==2:
            num=int(input("ingrese numero de la sucursal:"))
            arreglo.total(num)
        elif opcion==3:
            dia=int(input("ingrese dia de la semana(1 a 7):"))
            arreglo.factura(dia)
        elif opcion==4:
            arreglo.minimo()
        else: opcion==5
        arreglo.Total_Facturado()
        
        opcion=menuOptions()
