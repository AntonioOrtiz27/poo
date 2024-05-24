from gestor import *
def menu():
    op=int(input("""menu
          op 1.Ingrese datos
          ->"""))
    return op

if __name__ == "__main__":
    cajas = controlador()
    cajas.CuentaBancaria()
    c=cuil = input("Ingresa el CUIL para mostar nombre,apellido y saldo: ")
    if cuil == c:
        N = cajas.obtenerNombre(cuil)
        A = cajas.obtenerApellido(cuil)
        S = cajas.obtenerSaldo(cuil)
        print("Los datos de la cuenta son:")
        print("Nombre:", N)
        print("Apellido:", A)
        print("Saldo:", S)
