class CajaDeAhorro:
    def __init__(self, numero_cuenta, cuil, apellido, nombre, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.cuil = cuil
        self.apellido = apellido
        self.nombre = nombre
        self.saldo = saldo

    def mostrarDatos(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("CUIL:", self.cuil)
        print("Apellido:", self.apellido)
        print("Nombre:", self.nombre)
        print("Saldo:", self.saldo)

    def extraer(self, importe):
        if importe <= self.saldo:
            self.saldo -= importe
            print("Se extrajo {} pesos de la cuenta.".format(importe))
            return self.saldo
        else:
            print("No se puede extraer el importe especificado.")
            return -1

    def depositar(self, importe):
        if importe > 0:
            self.saldo += importe
            print("Se depositaron {} pesos en la cuenta.".format(importe))
        else:
            print("El importe a depositar debe ser mayor que cero.")

    def validarCuit(cuil):
        lista2 = [20,23,27,30]
        if(len(cuil) != 11 or int(cuil[0:2]) not in lista2 ):
            return False
        lista = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        a = 0
        for i in range(10):
            a += int(cuil[i]) * lista[i]

        b = a%11
        digitoV = 0
        
        if b == 0:
            digitoV = 0
        elif b == 1:
            if cuil[0:2] == '20':
                digitoV = 9
            elif cuil[0:2] == '27':
                digitoV = 4
            else:
                digitoV = 11 - b
        else:
            digitoV = 11 - b
    
        return int(cuil[10]) == digitoV


def test():
    cuentas = []
    for i in range(2):
        numero_cuenta = str(input("Ingrese el número de cuenta: "))
        cuil = str(input("Ingrese el CUIL: "))
                    
        cuil_valido = CajaDeAhorro.validarCuit(cuil)
        while not cuil_valido:
            print("El CUIL ingresado no es válido.")
            cuil = str(input("Ingrese el CUIL nuevamente: "))
            cuil_valido = CajaDeAhorro.validarCuit(cuil)
            
        print("El CUIL ingresado es válido.")
        apellido = str(input("Ingrese el apellido: "))
        nombre = str(input("Ingrese el nombre: "))
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        cuenta = CajaDeAhorro(numero_cuenta, cuil, apellido, nombre, saldo_inicial)
        cuentas.append(cuenta)
          
            
    for i in range(len(cuentas)):
        cuentas[i].mostrarDatos()
        cuentas[i].extraer(100)
        cuentas[i].depositar(500)
            
test()