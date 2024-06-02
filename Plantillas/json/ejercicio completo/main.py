from objectencoder import ObjectEncoder
from lista import Lista
from calefactor import *

if __name__ == "__main__":
    lista = Lista()
    encoder = ObjectEncoder()
    dic = encoder.leerJSONArchivo("calefactores.json")
    lista = encoder.decodificarDiccionario(dic)
    
    for i in lista:
        print(i)
        
    opcion = int(input("Opcion: "))
    while opcion != 0:
        if opcion == 1:
            try: 
                calefactor_electrico1 = CalefactorElectrico("MarcaA", "ModeloA1", "PaísA", 1500, "Tarjeta", 12, "Si", 2000)
                lista.insertar(calefactor_electrico1, 2)    
            except IndexError as e:
                print(e)
                
        if opcion == 2:
            tipo = input("Tipo (1.Electrico o 2.Gas): ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            pais = input("País: ")
            precio = float(input("Precio: "))
            forma_de_pago = input("Forma de pago: ")
            cuotas = int(input("Cuotas: "))
            promocion = input("Promoción: ")
            
            if tipo == "1":
                potencia = int(input("Potencia: "))
                calefactor = CalefactorElectrico(marca, modelo, pais, precio, forma_de_pago, cuotas, promocion, potencia)
            if tipo == "2":
                matricula = input("Matricula: ")
                calorias = int(input("Calorias: "))
                calefactor = CalefactorGas(marca, modelo, pais, precio, forma_de_pago, cuotas, promocion, matricula, calorias)
                
            lista.agregar(calefactor)
        
        if opcion == 3:
            try: 
                lista.mostrar_tipo(1)
            except IndexError as e:
                print(e)
        
        if opcion == 4:
            lista.mostrar_mejor()
        
        if opcion == 5:
            marca = input("Marca: ")
            lista.mostrar_marca(marca)
            
        if opcion == 6:
            lista.mostrar_promociones()
            
        if opcion == 7:
            encoder.guardarJSONArchivo(lista.to_dict(), "calefactores2.json")
            
        opcion = int(input("Opcion: "))