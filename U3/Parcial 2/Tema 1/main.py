from claseLista import Lista
from claseCasa import *
from claseDepartamento import *

def test():
    opcion = int(input("""Ingrese opcion: 
        1_insertar inmuebles a la coleccion
        2_Mostrar coleccion de inmuebles insertados.
        3_Insertar un inmueble al final de la lista.
        4_Mostrar coleccion de inmuebles insertados.
        5_Departamentos con cantidad de dormitorios inferior, a una ingresada.
        6_Mostrar inciso 3
        7_
        0_Para finalizar
        ----->""")) 
    return opcion 
    
if __name__ == '__main__':
    lista = Lista()
      
    op=test()
    #insertar por posición Manuel,al final pos-1 o a la cabeza pos.
    while op != 0:
        if op == 1:
            pos=int(input("ingrese la posicion donde insertar:"))
            dato=str(input("ingrese el dato a insertar en la lista(Dpto o Casa):"))
            localidad=input("ingrese localidad:")
            direccion=input("ingrese direccion:")
            superficie=float(input("ingrese superficie:"))
            if dato == "casa":
                metros=input("ingrese metros:")
                casita= Casa(localidad,direccion,superficie,metros)
                lista.insertar(pos,casita)
            elif dato == "departamento":
                cantidad=input("ingrese cantidad:")
                numero=input("ingrese numero monoblock:")
                depa=input("ingrese num depa:")
                piso=input("ingrese num piso:")
                departamento =Departamento(localidad,direccion,superficie,cantidad,numero,depa,piso)
                lista.insertar(pos,departamento )
            else:
                print("Tipo de inmueble no reconocido.")
        elif op==2:
            print("Inmuebles insertados.")
            for inmuebles in lista:
                print(f"{inmuebles}\n")
        elif op == 3:
            elemento=str(input("ingrese un tipo de inmueble"))
            localidad=input("ingrese localidad:")
            direccion=input("ingrese direccion:")
            superficie=input("ingrese superficie:")
            if elemento == "casa":
                metros=input("ingrese metros:")
                casita= Casa(localidad,direccion,superficie,metros)
                lista.agregar_uno(casita)
            elif elemento == "departamento":
                cantidad=input("ingrese cantidad dormitorios:")
                numero=input("ingrese numero monoblock:")
                depa=input("ingrese num depa:")
                piso=input("ingrese num piso:")
                departamento =Departamento(localidad,direccion,superficie,cantidad,numero,depa,piso)
                lista.agregar_uno(departamento)
            else:
                print("Tipo de inmueble no reconocido.")
            print("elemento insertado al final de la lista")
        elif op==4:
            for inmuebles in lista:
                print(f"{inmuebles}\n")
        elif op==5:
            cantidad=int(input("Ingrese cantidad de dormitorios:"))
            lista.total(cantidad)
        elif op==6:
            lista.mostrar()
        op=test()

#insertar por posicion manual al principio de la lista
'''
1
1
casa
capital
angel del rojas
300
600
1
0
casa
rivadavia
san lorenzo
500
1000
1
2
casa
chimbas
casa gordo alaniz
1000
2000
1
3
departamento
angaco
coperal 4
5
10
1
10
8
1
4
departamento
iglesia
coperal 4
5
10
1
10
8
2
'''

#insertar al final
'''
casa
cueva
chancho
1000
2000
4
'''