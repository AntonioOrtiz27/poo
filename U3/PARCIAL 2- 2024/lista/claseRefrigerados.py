from claseProductos import Producto

class Refrigerado(Producto):
    __codigo: int
    
    def __init__(self,Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo,Codigo):
        super().__init__ (Nombre, FechaE, FechaV, Temperatura, Pais, NumLote, Costo)
        self.__codigo = Codigo    
        
    def __str__(self):
        return super().__str__() + f"{self.__codigo} "
    
    
    #Importe de venta de un producto refrigerado: el costo base, 
    # menos el 10% si la fecha de vencimiento es dentro de dos meses 
    #(Mes de vencimiento -Mes actual). 
    #Caso contrario el importe de venta es: precio base+ 1%
    def importe(self):
        fecha_vencimiento = self.getFechavencimiento().split('/')
        fecha_actual = "01/06/2024".split('/')  # Suponiendo que la fecha actual es 01/06/2024 para esta implementación

        anio_vencimiento = int(fecha_vencimiento[2])
        mes_vencimiento = int(fecha_vencimiento[1])

        anio_actual = int(fecha_actual[2])
        mes_actual = int(fecha_actual[1])

        # Calcular la diferencia en meses
        meses_diferencia = (anio_vencimiento - anio_actual) * 12 + (mes_vencimiento - mes_actual)

        if meses_diferencia <= 2:
            importe_venta = super().getCosto() * 0.9
        else:
            importe_venta =  super().getCosto() * 1.01
        
        return round(importe_venta, 2)
