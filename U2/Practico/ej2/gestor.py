from clase import *

class controlador:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregar(self, una_caja):
        self.__lista.append(una_caja)

    def CuentaBancaria(self):
        encontrado:bool=True
        if encontrado==True:
            cuil = input("Ingresa el CUIL: ")
            nombre = input("Ingresa el nombre: ")
            apellido = input("Ingresa el apellido: ")
            saldo = float(input("Ingresa el saldo: "))
            self.agregar(cuenta(cuil, nombre, apellido, saldo))
            return cuil


    def obtenerNombre(self, cuil):
        for caja in self.__lista:
            if caja.ObtenerCuil() == cuil:
                return caja.ObtenerNombre()
            
    def obtenerApellido(self,cuil):
        for caja in self.__lista:
            if caja.ObtenerCuil() == cuil:
                return caja.ObtenerApellido()
            
    def obtenerSaldo(self,cuil):
        for caja in self.__lista:
            if caja.ObtenerCuil() == cuil:
                return caja.ObtenerSaldo()